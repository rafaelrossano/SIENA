from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Any

from app.db.session import get_db
from app.schemas.user import UserSchema, UserResponse, UserPublic
from app.services.user_service import UserService
from app.exceptions import UserAlreadyExistsException, DatabaseOperationException, UserNotFoundException
from app.api.dependencies import get_current_user

router = APIRouter()

@router.post(
    "/create",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
    description="Create a new user with a username and password.",
)
def create_user(
    user_in: UserSchema,
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
        
@router.put(
    "/{user_id}", response_model=UserPublic)
def update_user(
    user_id: int,
    user_data: UserSchema,
    session: Session = Depends(get_db),
    current_user = Depends(get_current_user),
) -> Any:
    """
    Update an existing user account.
    
    ## Path Parameters
    - **user_id**: Unique identifier for the user to update
    
    ## Request Body
    - **username**: Unique username (3-16 characters)
    - **password**: Secure password (8+ characters with uppercase, lowercase, and numbers)
    
    ## Returns
    Updated user object if successful.
    
    ## Errors
    - **404 Not Found**: User not found
    - **500 Internal Server Error**: Database operation failed
    """
    if current_user.id != user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to update this user."
        )
    
    try:
        user = UserService.update_user(db=session, user_id=user_id, user_data=user_data)
        return user
    except UserNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message
        )
    except DatabaseOperationException as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=e.message
        )