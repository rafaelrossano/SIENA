from typing import Optional
from sqlalchemy.orm import Session

from app.models import User

class UserRepository:
    """
    Repository for user-related database operations.
    """

    @staticmethod
    def get_by_username(db: Session, username: str) -> Optional[User]:
        """
        Retrieve a user by username.
        
        Args:
            db: Database session
            username: Username of the user to retrieve
            
        Returns:
            User object if found, None otherwise
        """
        return db.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_by_id(db: Session, user_id: int) -> Optional[User]:
        """
        Retrieve a user by ID.
        
        Args:
            db: Database session
            user_id: ID of the user to retrieve
            
        Returns:
            User object if found, None otherwise
        """
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def create_user(db: Session, username: str, hashed_password: str) -> User:
        """
        Create a new user in the database.
        
        Args:
            db: Database session
            user: User object to create
            
        Returns:
            Created User object
        """
        user = User(username=username, hashed_password=hashed_password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def update_user(db: Session, user: User, username: str, hashed_password: str) -> User:
        """
        Update an existing user in the database.
        
        Args:
            db: Database session
            user: User object with updated information
            
        Returns:
            Updated User object
        """
        user.username = username
        user.hashed_password = hashed_password
        db.commit()
        db.refresh(user)
        return user
