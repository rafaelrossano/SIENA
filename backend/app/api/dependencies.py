from fastapi import Depends, HTTPException, status, security
from fastapi.security import OAuth2PasswordBearer
from jwt import decode
from jwt.exceptions import PyJWTError

from sqlalchemy.orm import Session
from typing import Annotated

from app.db.session import get_db
from app.models import User
from app.repository import UserRepository
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/token")

def get_current_user(
    session: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode(token, settings.TOKEN_SECRET_KEY, algorithms=[settings.TOKEN_ALGORITHM])
        print(payload)
        
        username: str = payload.get("sub")
        if not username:
            raise credentials_exception

    except PyJWTError:
        raise credentials_exception

    user = UserRepository.get_by_username(session, username=username)
    if user is None:
        raise credentials_exception
    
    return user