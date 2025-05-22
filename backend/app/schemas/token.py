from pydantic import BaseModel, Field

class Token(BaseModel):
    """
    Schema for token response.
    
    Attributes:
        access_token: The JWT access token
        token_type: The type of the token (usually "bearer")
    """
    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(default="bearer", description="Type of the token")