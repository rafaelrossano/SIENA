from fastapi import Depends, HTTPException, status, security
from fastapi.security import OAuth2PasswordBearer
import jwt

from sqlalchemy.orm import Session
from typing import Annotated

from app.db.session import get_db
from app.models import User
from app.repository import UserRepository
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(
    session: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)):
    ...
