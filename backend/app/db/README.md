# Database Configuration

This folder contains the configuration and functionality related to the SQLite database using SQLAlchemy.

## Files and their functions

- `__init__.py`: Exports the main classes and functions to facilitate imports
- `database.py`: Defines the database connection and creates the SQLAlchemy engine
- `session.py`: Provides functions to manage database sessions
- `init_db.py`: Functions for database initialization and manual migrations

## Usage

To use the database in a route or service, import the following:

```python
from app.db.session import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    # Use the db session here to access the database
    pass
```

## Database file location

As defined in the `SQLITE_DATABASE_URL` environment variable, the SQLite database file is located at:

```
app/database.db
```

## Database initialization

To initialize the database during application startup:

```python
from app.db.init_db import init_db

init_db()
```
