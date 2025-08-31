"""Pydantic models"""

from enum import Enum

from pydantic import BaseModel


class StatusEnum(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"


class TodoDataModel(BaseModel):
    title: str  # Title of todo 
    content: str = "No description..."  # Longer description (Optional)
    created_at: str  # Time created
    edited_at: str  # Time created
    status: StatusEnum  # To do, In progress, Done


class TodoCreateRequest(BaseModel):
    title: str  # Title of todo 
    content: str = "No description..."  # Longer description (Optional)
    status: StatusEnum  # To do, In progress, Done
    
    
class TodoUpdateRequest(BaseModel):
    id: int  # Todo row ID
    field: str  # Field to edit
    new_value: str  # New field value


class TodoDeleteRequest(BaseModel):
    id: int  # Todo row ID