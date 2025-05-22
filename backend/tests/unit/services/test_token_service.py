from datetime import timedelta
import pytest
import time
import jwt

from app.services.auth.token_service import create_access_token
from app.core.config import settings

def test_create_access_token():
    """
    Test the creation of an access token.
    """
    data = {"sub": "test_user"}
    token = create_access_token(data)
    
    decoded = jwt.decode(token, settings.TOKEN_SECRET_KEY, algorithms=[settings.TOKEN_ALGORITHM])
    
    assert decoded["sub"] == data["sub"]
    assert "exp" in decoded
    
test_create_access_token()