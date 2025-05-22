from app.db.database import SessionLocal

def get_db():
    """
    Dependency to obtain a database session.
    
    Yields:
        SQLAlchemy Session: A database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
