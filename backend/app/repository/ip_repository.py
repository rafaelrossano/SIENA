from typing import List, Optional
from sqlalchemy import func, update
from sqlalchemy.orm import Session
from sqlalchemy.dialects.sqlite import insert

from app.models import IPAddress

