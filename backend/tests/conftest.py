import sys
import os

import asyncio
import os
from typing import Generator, AsyncGenerator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.pool import StaticPool

from app.db.database import Base
from app.db.session import get_db
from main import app
from app.services.auth.token_service import create_access_token
from app.models import User
from app.services.auth.password_service import get_password_hash

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

# Usar banco de dados em memória para testes
TEST_DATABASE_URL = "sqlite:///:memory:"

# Cria engine de banco de dados específica para os testes
engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db() -> Generator:
    """
    Fixture para criar e fornecer uma sessão de banco de dados para testes.
    """
    # Cria todas as tabelas para cada teste
    Base.metadata.create_all(bind=engine)
    
    # Cria uma sessão de teste
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        # Limpa as tabelas após o teste
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db) -> Generator:
    """
    Fixture para criar e fornecer um cliente de teste.
    """
    # Injeta a sessão de banco de dados de teste na aplicação
    def override_get_db():
        try:
            yield db
        finally:
            pass
    
    # Substitui a dependência original pelo override para testes
    app.dependency_overrides[get_db] = override_get_db
    
    # Fornece um cliente de teste
    with TestClient(app) as c:
        yield c
    
    # Limpa as substituições de dependências após o teste
    app.dependency_overrides = {}

@pytest.fixture
def test_user(db) -> User:
    """
    Fixture para criar um usuário de teste no banco.
    """
    pwd = "rafael2006"
    user = User(
        username="testuser",
        hashed_password=get_password_hash(pwd),
        is_active=True,
        is_admin=False
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    
    user.clean_password = pwd
    return user

@pytest.fixture
def admin_user(db) -> User:
    """
    Fixture para criar um usuário administrador de teste no banco.
    """
    user = User(
        username="adminuser",
        hashed_password="$2b$12$GMbu.ZTkEYvMIYFE17B/lOBpGYnS8g5TnWXkTgCnc0zQQQ5z1RHm2",  # "password"
        is_active=True,
        is_admin=True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@pytest.fixture
def token_for_user(test_user) -> str:
    """
    Fixture para criar um token válido para o usuário de teste.
    """
    return create_access_token({"sub": test_user.username})

@pytest.fixture
def token_for_admin(admin_user) -> str:
    """
    Fixture para criar um token válido para o usuário administrador.
    """
    return create_access_token({"sub": admin_user.username})