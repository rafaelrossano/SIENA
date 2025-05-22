class UserException(Exception):
    """Base class for user-related exceptions."""
    pass

class UserAlreadyExistsException(UserException):
    """Exception raised when attempting to create a user that already exists."""
    def __init__(self, username: str):
        self.username = username
        self.message = f"User with username '{username}' already exists"
        super().__init__(self.message)
        
class InvalidCredentialsException(UserException):
    """Exception raised when authentication fails."""
    def __init__(self):
        self.message = "Invalid username or password"
        super().__init__(self.message)
        
class UserNotFoundException(UserException):
    """Exception raised when a user is not found."""
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.message = f"User with ID '{user_id}' not found"
        super().__init__(self.message)