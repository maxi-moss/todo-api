"""Pydantic models"""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class StatusEnum(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"


class TodoModel(BaseModel):
    id: int = None  # Optional (primary key)
    title: str  # Title of todo 
    content: str = "No description"  # Longer description (Optional)
    created_at: datetime  # Time created
    edited_at: datetime  # Time created
    status: StatusEnum  # To do, In progress, Done