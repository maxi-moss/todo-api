"""Utility functions for notes"""

from datetime import datetime

from note.schemas import NoteDataModel


async def build_data_model(title: str, content: str) -> NoteDataModel:
    """Create data model for insertion into database"""
    current_time = str(datetime.now())
    data = {
        "title": title,
        "content": content,
        "created_at": current_time,
        "edited_at": current_time
    }
    return data