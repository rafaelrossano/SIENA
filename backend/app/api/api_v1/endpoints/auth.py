from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.db import get_db

router = APIRouter()

@router.post(
    "/token",
    response_model=dict,
    status_code=status.HTTP_200_OK,
    summary="Generate access token",
    description="Generate an access token using username and password.",
)