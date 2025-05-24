from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class ProfileSchema(BaseModel):
    """
    Schema for user profile data.
    """
    username: str = Field(..., min_length=3, max_length=16, description="Username of the user")
    full_name: Optional[str] = Field(None, max_length=100, description="Full name of the user")
    email: Optional[EmailStr] = Field(None, description="Email address of the user")
    city: Optional[str] = Field(None, max_length=100, description="City of the user")
    state: Optional[str] = Field(None, max_length=2, description="State of the user")
    associated_accounts: Optional[list[str]] = Field(None, description="List of associated accounts")
    ip_addresses: Optional[list[str]] = Field(None, description="List of IP addresses associated with the user")
    

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "johndoe@example.com",
                "full_name": "John Doe",
                "city": "Rio de Janeiro",
                "state": "RJ",
                "associated_accounts": ["OldAccountJohn", "DoeTrampolin"],
                "ip_addresses": ["192.168.1.1", "10.0.0.1"]
            }
        }
        
class ProfileResponse(BaseModel):
    """
    Response schema for user profile data.
    """
    id: int
    username: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
            }
        }
