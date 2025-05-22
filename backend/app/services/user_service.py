from typing import Optional
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.services.auth.password_service import get_password_hash, verify_password
from app.repository import UserRepository
from app.exceptions import UserAlreadyExistsException, InvalidCredentialsException, DatabaseOperationException

class UserService:
    """
    Service for handling user-related business logic including authentication.
    """
    
    @staticmethod
    def create_user(db: Session, user_data: UserCreate) -> User:
        """
        Create a new user with a hashed password.
        
        Args:
            db: Database session
            user_data: User data including username and password
            
        Returns:
            Created user object
        """
        existing_user = UserRepository.get_by_username(db, username=user_data.username)
        if existing_user:
            raise UserAlreadyExistsException(username=user_data.username)
        hashed_password = get_password_hash(user_data.password)
        
        try:
            user = UserRepository.create_user(
                db=db,
                username=user_data.username,
                hashed_password=hashed_password
            )
            return user
        except Exception as e:
            db.rollback()
            raise DatabaseOperationException(f"Error creating user: {str(e)}")
