from enum import Enum as PyEnum
from datetime import datetime
from sqlalchemy import String, Integer, ForeignKey, DateTime, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base

class AccountType(str, PyEnum):
    """
    Enum representing the type of account.
    """
    PRIMARY = "primary"
    PREVIOUS = "previous"
    FAKE = "fake"

class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
        comment="Unique identifier for the account"
    )
    
    profile_id: Mapped[int] = mapped_column(
        ForeignKey("profiles.id"),
        nullable=False,
        comment="Foreign key to the profile table"
    )

    nickname: Mapped[str] = mapped_column(
        String(16),
        nullable=False,
        comment="Nickname of the account"
    )
    
    is_active: Mapped[bool] = mapped_column(
        nullable=False,
        default=True,
        comment="Indicates if the account is active"
    )
    
    account_type: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
        default=AccountType.PRIMARY.value,
        comment="Type of the account (primary, previous, fake)"
    )
