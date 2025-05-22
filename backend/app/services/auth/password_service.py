from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    """
    Hashes a password using bcrypt.
    
    Args:
        password (str): The password to hash.
        
    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against a hashed password.
    
    Args:
        plain_password (str): The plain password to verify.
        hashed_password (str): The hashed password to verify against.
        
    Returns:
        bool: True if the password is valid, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)
