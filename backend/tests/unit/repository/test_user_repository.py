import pytest
from sqlalchemy.orm import Session

from app.repository.user_repository import UserRepository
from app.models import User

def test_get_by_username_existing_user(db: Session, test_user: User):
    # Act
    result = UserRepository.get_by_username(db, test_user.username)
    
    # Assert
    assert result is not None
    assert result.username == test_user.username
    
def test_get_by_username_nonexistent_user(db: Session):
    """Test retrieving a non-existent user by username."""
    # Act
    result = UserRepository.get_by_username(db, "nonexistent")
    
    # Assert
    assert result is None
    
def test_create_user(db: Session):
    """Test creating a new user."""
    # Arrange
    username = "newuser"
    hashed_password = "hashed_password_value"
    
    # Act
    result = UserRepository.create_user(db, username, hashed_password)
    
    # Assert
    assert result is not None
    assert result.username == username
    assert result.hashed_password == hashed_password
    
    # Verify user was added to DB
    retrieved = db.query(User).filter(User.username == username).first()
    assert retrieved is not None
    assert retrieved.username == username
    assert retrieved.hashed_password == hashed_password