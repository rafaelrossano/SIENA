from datetime import datetime
from typing import Optional
from sqlalchemy import Integer, String, ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
        comment="Unique identifier for the profile"
    )
    
    
    full_name: Mapped[str] = mapped_column(
        String(128),
        nullable=True,
        comment="Full name of the profile"
    )
    

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=True,
        comment="City of the profile"
    )
    
    
    state: Mapped[str] = mapped_column(
        String(2),
        nullable=True,
        comment="State of the profile"
    )
    
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        comment="Timestamp when the profile was created"
    )

    
    ip_adress: Mapped[list["IPAddress"]] = relationship( # type: ignore
        "IPAddress",
        back_populates="profile",
        cascade="all, delete-orphan",
        lazy="dynamic"
    )
    
    
    @property
    def current_account(self) -> Optional["Account"]:
        """
        Returns the current primary account associated with the profile.
        """
        primary_accounts = [acc for acc in self.accounts 
                          if acc.account_type == "primary" and acc.is_active]
        return primary_accounts[0] if primary_accounts else None
    
    @property
    def previous_accounts(self) -> list["Account"]:
        """
        Returns a list of previous accounts associated with the profile.
        """
        return [acc for acc in self.accounts 
                if acc.account_type == "previous"]
        
    @property
    def fake_accounts(self) -> list["Account"]:
        """
        Returns a list of fake accounts associated with the profile.
        """
        return [acc for acc in self.accounts 
                if acc.account_type == "fake"]