from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Create SQLAlchemy engine using SQLite URL
engine = create_engine(
    settings.SQLITE_DATABASE_URL,
    connect_args={"check_same_thread": False}  # Required only for SQLite
)

# Create SessionLocal class for database session instances
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for declarative models
Base = declarative_base()
