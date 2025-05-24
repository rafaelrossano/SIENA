from typing import Optional

from sqlalchemy.orm import Session

from app.models import Profile
from app.schemas.profile_schema import ProfileSchema

class ProfileRepository:
    @staticmethod
    def get_by_username(db: Session, username: str) -> Optional[Profile]:
        """
        Retrieve a profile by username.
        
        Args:
            db: Database session
            username: Username of the profile to retrieve
            
        Returns:
            Profile object if found, None otherwise
        """
        return db.query(Profile).filter(Profile.username == username).first()
    
    @staticmethod
    def create_profile(db: Session, profile: ProfileSchema) -> Profile:
        """
        Create a new profile in the database.
        
        Args:
            db: Database session
            profile: Profile object to create
            
        Returns:
            Created Profile object
        """
        profile = Profile(**profile.model_dump())
        db.add(profile)
        db.commit()
        db.refresh(profile)
        return profile