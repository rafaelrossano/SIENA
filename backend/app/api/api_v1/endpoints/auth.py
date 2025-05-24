from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db import get_db
from app.repository import UserRepository
from app.services.auth.password_service import verify_password
from app.services.auth.token_service import create_access_token
from app.schemas.token import Token



router = APIRouter()

@router.post(
    "/token",
    response_model=Token,
    # status_code=status.HTTP_200_OK,
    # summary="Generate access token",
    # description="Generate an access token using username and password.",
)
def login_for_access_token(
    db: Session = Depends(get_db),
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    """
    Generate an access token for the user.
    
    ## Request Body
    - **username**: Username of the user
    - **password**: Password of the user
    
    ## Returns
    Access token if successful.
    
    ## Errors
    - **401 Unauthorized**: Invalid credentials
    """
    user = UserRepository.get_by_username(db, username=form_data.username)
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}