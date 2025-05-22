"""
Exception classes for the application.

This module provides custom exception classes that represent
various error conditions in the application domain.
"""

from .user_exceptions import (
    UserException,
    UserAlreadyExistsException,
    InvalidCredentialsException,
    UserNotFoundException
)

from .database_exceptions import (
    DatabaseException,
    DatabaseOperationException,
)

__all__ = [
    "UserException",
    "UserAlreadyExistsException",
    "InvalidCredentialsException",
    "UserNotFoundException",
    "DatabaseException",
    "DatabaseOperationException",
]