"""Utility functions for todos"""

from datetime import datetime

from todo.schemas import TodoDataModel


async def build_data_model(title: str, content: str, status: str) -> TodoDataModel:
    """Create data model for insertion into database"""
    current_time = str(datetime.now())
    data = {
        "title": title,
        "content": content,
        "created_at": current_time,
        "edited_at": current_time,
        "status": status
    }
    return data