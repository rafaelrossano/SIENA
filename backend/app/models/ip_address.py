from sqlalchemy import Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

class IPAddress(Base):
    """
    Represents an IP address in the database.
    """
    __tablename__ = "ip_addresses"
    
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
        comment="Unique identifier for the IP address"
    )
    
    profile_id: Mapped[int] = mapped_column(
        ForeignKey("profiles.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
        comment="Foreign key referencing the profile"
    )
    
    ip_address: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
        comment="IP address in string format"
    )
    
    
    timestamp: Mapped[DateTime] = mapped_column(
        DateTime,
        server_default=func.now(),
        comment="Timestamp when the IP address was created"
    )
    
    
    profile = relationship("Profile", back_populates="ip_addresses")