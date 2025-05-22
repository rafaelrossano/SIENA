class DatabaseException(Exception):
    """Base class for database-related exceptions."""
    pass

class DatabaseOperationException(DatabaseException):
    """Exception raised when a database operation fails."""
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)