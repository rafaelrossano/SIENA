import re
from typing import Any, Dict
from pydantic import BaseModel, Field, field_validator, ConfigDict

class UserSchema(BaseModel):
    """
    Schema for user creation requests.
    
    Attributes:
        username: User's unique identifier, 3-16 characters
        password: User's password, must meet security requirements (Uppercase, lowercase, number, special character)
    """
    username: str = Field(..., min_length=3, max_length=16, description="Unique username")
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
                "username": "string",
                "password": "string"
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
        # Check each requirement separately
        has_uppercase = any(c.isupper() for c in password)
        has_lowercase = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)
        
        # Collect all failed requirements
        errors = []
        if not has_uppercase:
            errors.append("uppercase letter")
        if not has_lowercase:
            errors.append("lowercase letter")
        if not has_digit:
            errors.append("digit")
        if not has_special:
            errors.append("special character")
        
        # Raise error if any requirements failed
        if errors:
            raise ValueError(
                f"Password must contain at least one {', one '.join(errors)}"
            )
        
        return password

class UserResponse(BaseModel):
    """
    Schema for user response.
    
    Attributes:
        id: Unique identifier for the user
        username: User's unique identifier
        is_active: Indicates if the user is active
    """
    id: int
    username: str
    is_active: bool

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "username": "johndoe",
                "is_active": True
            }
        }
    )
    
class UserPublic(BaseModel):
    """
    Public schema for user data.
    
    Attributes:
        id: Unique identifier for the user
        username: User's unique identifier
        is_active: Indicates if the user is active
        is_admin: Indicates if the user is an admin
    """
    id: int
    username: str
    is_active: bool
    is_admin: bool = Field(default=False)

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "username": "johndoe",
                "is_active": True,
                "is_admin": False
            }
        }
    )