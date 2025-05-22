from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from jwt import encode

from app.core.config import settings

SECRET_KEY = settings.TOKEN_SECRET_KEY
ALGORITHM = settings.TOKEN_ALGORITHM
TOKEN_EXPIRE_MINUTES = int(settings.TOKEN_EXPIRE_MINUTES)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Create a JWT access token.

    Args:
        data (dict): Data to encode in the token.
        expires_delta (timedelta | None): Expiration time delta.

    Returns:
        str: Encoded JWT access token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(tz=ZoneInfo("UTC")) + expires_delta
    else:
        expire = datetime.now(tz=ZoneInfo("UTC")) + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt