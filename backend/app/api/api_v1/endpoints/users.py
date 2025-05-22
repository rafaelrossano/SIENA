from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Any

from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService
from app.exceptions import UserAlreadyExistsException, DatabaseOperationException

router = APIRouter()

@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description="Create a new user with a username and password.",
)
def create_user(
    user_in: UserCreate,
    db: Session = Depends(get_db),
) -> Any:
    """
    Create a new user account.
    
    ## Request Body
    - **username**: Unique username (3-50 characters)
    - **password**: Secure password (8+ characters with uppercase, lowercase, and numbers)
    
    ## Returns
    User object with ID and username if successful.
    
    ## Errors
    - **409 Conflict**: Username already exists
    - **500 Internal Server Error**: Database operation failed
    """
    try:
        user = UserService.create_user(db=db, user_data=user_in)
        return user
    except UserAlreadyExistsException as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
    except DatabaseOperationException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message
        )