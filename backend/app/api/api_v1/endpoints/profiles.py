from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Profile
from app.schemas.profile_schema import ProfileSchema, ProfileResponse
from app.api.dependencies import get_current_user

router = APIRouter()

@router.post(
    "/create",
    response_model=ProfileResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new profile",
    description="Create a new profile with the given details.",
)
def create_profile(
    profile_in: ProfileSchema,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
) -> ProfileResponse:
    """
    Create a new profile.
    
    ## Request Body
    - **username**: Username (3-16 characters)
    - **full_name**: Full name (optional)
    - **email**: Email address (optional)
    - **city**: City (optional)
    - **state**: State - 2 letters (optional)
    - **associated_accounts**: Comma-separated list of associated accounts (optional)
    - **ip_addresses**: Comma-separated list of IP addresses (optional)
    
    ## Returns
    Profile object with ID and details if successful.
    
    ## Errors
    - **409 Conflict**: Username already exists
    - **500 Internal Server Error**: Database operation failed
    """
    existing_profile = db.query(Profile).filter(Profile.username == profile_in.username).first()
    
    if existing_profile:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already exists",
        )
    
    new_profile = Profile(**profile_in.dict())
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    
    return new_profile