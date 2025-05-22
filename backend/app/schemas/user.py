import re
from typing import Any, Dict
from pydantic import BaseModel, Field, field_validator, ConfigDict

class UserCreate(BaseModel):
    """
    Schema for user creation requests.
    
    Attributes:
        username: User's unique identifier, 3-50 characters
        password: User's password, must meet security requirements
    """
    username: str = Field(..., min_length=3, max_length=50, description="Unique username")
    password: str = Field(
        ..., 
        min_length=8, 
        max_length=128, 
        description="Password that meets security requirements"
    )

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "username": "johndoe",
                "password": "StrongPassword123"
            }
        }
    )

    @field_validator("password")
    def validate_password(cls, password: str) -> str:
        """
        Validate that the password meets security requirements.
        
        Args:
            password: The password to validate
            
        Returns:
            The validated password
            
        Raises:
            ValueError: If password doesn't meet security requirements
        """
        # At least 8 chars, 1 uppercase, 1 lowercase, 1 digit, and 1 special character
        pattern = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-Za-z\d]{8,}$")
        if not pattern.match(password):
            raise ValueError(
                "Password must be at least 8 characters long and contain uppercase letters, "
                "lowercase letters, number and special character."
            )
        return password
