"""Pydantic models"""

from pydantic import BaseModel


class NoteModel(BaseModel):
    title: str  # Title of todo 
    content: str  # Full note content
    created_at: str  # Time created
    edited_at: str  # Time last edited