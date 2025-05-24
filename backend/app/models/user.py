from datetime import datetime
from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.database import Base

class User(Base):
    """
    User model representing a user in the system.
    """
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True, 
        index=True,
        comment="Unique identifier for the user"
    )
    
    username: Mapped[str] = mapped_column(
        String(16), 
        unique=True, 
        index=True, 
        comment="Unique user's username"
    )
    
    hashed_password: Mapped[str] = mapped_column(
        String(128), 
        comment="Hashed password for the user"
    )
    
    is_active: Mapped[bool] = mapped_column(
        default=True, 
        comment="Flag indicating if the user is active"
    )
    
    is_admin: Mapped[bool] = mapped_column(
        default=False, 
        comment="Flag indicating if the user is an admin"
    )
    
    core_tag: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
        comment="Core tag associated with the user"
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime, 
        server_default=func.now(), 
        comment="Timestamp when the user was created"
    )