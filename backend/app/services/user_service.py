from typing import Optional
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserSchema
from app.services.auth.password_service import get_password_hash, verify_password
from app.repository import UserRepository
from app.exceptions import UserAlreadyExistsException, InvalidCredentialsException, DatabaseOperationException, UserNotFoundException

class UserService:
    """
    Service for handling user-related business logic including authentication.
    """
    
    @staticmethod
    def create_user(db: Session, user_data: UserSchema) -> User:
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


    @staticmethod
    def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
        """
        Authenticate a user by verifying the username and password.
        
        Args:
            db: Database session
            username: Username of the user
            password: Password of the user
            
        Returns:
            Authenticated user object if successful, None otherwise
        """
        user = UserRepository.get_by_username(db, username=username)
        if not user or not verify_password(password, user.hashed_password):
            raise InvalidCredentialsException()
        
        return user
    
    @staticmethod
    def update_user(db: Session, user_id: int, user_data: UserSchema) -> User:
        """
        Update an existing user's information.
        
        Args:
            db: Database session
            user_id: ID of the user to update
            user_data: New user data
            
        Returns:
            Updated user object
        """
        user = UserRepository.get_by_id(db, user_id=user_id)
        if not user:
            raise UserNotFoundException(user_id=user_id)
        
        try:
            updated_user = UserRepository.update_user(
                db=db,
                user=user,
                username=user_data.username,
                hashed_password=get_password_hash(user_data.password)
            )
            return updated_user
        except Exception as e:
            db.rollback()
            raise DatabaseOperationException(f"Error updating user: {str(e)}")