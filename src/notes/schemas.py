"""Pydantic models"""

from datetime import datetime

from pydantic import BaseModel


class NoteModel(BaseModel):
    id: int
    title: str  # Title of todo 
    content: str  # Full note content
    created_at: str  # Time created
    edited_at: datetime  # Time last edited