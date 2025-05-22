import pytest
from sqlalchemy.orm import Session

user = {
  "id": 1,
  "username": "Torvi.",
  "is_active": True
}

def test_get_token(client, test_user):
    response = client.post(
        "/api/v1/auth/token",
        data={
            "username": test_user.username,
            "password": test_user.clean_password,
        }
    )
    token = response.json()
    
    assert response.status_code == 200
    assert token['token_type'] == 'bearer'
    assert 'access_token' in token