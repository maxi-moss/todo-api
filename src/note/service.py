"""Business logic"""

from typing import Optional
from functools import lru_cache
import logging

from common.crud_interface import CRUD
from database.service import get_db_service
from note.utils import build_data_model

logger = logging.getLogger(__name__)


class NoteService(CRUD):
    def __init__(self):
        self.db_client = get_db_service()
        
    async def create(self, title: str, content: Optional[str] = ""):
        """
        Create a note and add it to the database.
        
        Args:
            title (str): Note title.
            content (str): Optional note content (Defaults to "").
        """
        try:
            data = await build_data_model(title, content)
            inserted_data = await self.db_client.insert(type="note", data=data)
            logger.info(f"Successfully inserted data: {inserted_data}")
        except Exception as e:
            logger.error(f"Error when creating note: {e}")
        return inserted_data
        
    async def get(self, id: int, fields: Optional[str] = "*"):
        """
        Get note contents from the database.
        
        Args:
            id (int): Note row id.
            fields (str): Field values to select from row (Defaults *).
        """
        try:
            note_content = await self.db_client.select(id=id, type="note", fields=fields)
            logger.info(f"Successfully read data: {note_content}")
        except Exception as e:
            logger.error(f"Error when reading note {e}")
        return note_content
          
    async def update(self, id: int, field: str, new_value: str):
        """
        Update a note entry in the database.
        
        Args:
            id (int): Note row id.
            field (str): Field to update.
            new_value (str): Updated field value.
        """
        try:
            updated_data = await self.db_client.update(id=id, type="note", field=field, value=new_value)
            logger.info(f"Successfully updated data: {updated_data}")
        except Exception as e:
            logger.error(f"Error when updating note {e}")
        return updated_data
    
    async def delete(self, id):
        """
        Delete a note from the database.
        
        Args:
            id (int): Note row id.
        """
        try:
            deleted_data = await self.db_client.delete(id=id, type="note")
            logger.info(f"Successfully deleted data: {deleted_data}")
        except Exception as e:
            logger.error(f"Error when deleting note {e}")
        return deleted_data
    
    
@lru_cache
def get_note_service():
    return NoteService()