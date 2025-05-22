import logging
from typing import Callable
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

def init_db() -> None:
    """
    Initialize the database.
    Creates all tables if they don't exist.
    """
    from app.db.database import Base, engine
    
    logger.info("Creating database tables")
    Base.metadata.create_all(bind=engine)
    logger.info("Tables created successfully")

def run_migration(func: Callable[[Session], None]) -> None:
    """
    Execute a manual database migration.
    
    Args:
        func: A function that takes a database session and executes operations.
    """
    from app.db.session import SessionLocal
    
    db = SessionLocal()
    try:
        func(db)
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"Error during migration: {e}")
        raise
    finally:
        db.close()
