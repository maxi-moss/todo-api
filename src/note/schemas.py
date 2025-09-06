"""Pydantic models"""

from pydantic import BaseModel


class NoteDataModel(BaseModel):
    title: str  # Title of note 
    content: str  # Full note content
    created_at: str  # Time created
    edited_at: str  # Time last edited


class NoteCreateRequest(BaseModel):
    title: str  # Title of note 
    content: str = ""  # Full note content (Optional)
    
    
class NoteUpdateRequest(BaseModel):
    id: int  # Note row ID
    field: str  # Field to edit
    new_value: str  # New field value


class NoteDeleteRequest(BaseModel):
    id: int  # Note row ID