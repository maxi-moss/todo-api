"""Business logic"""

from typing import Optional
from functools import lru_cache
import logging

from common.crud_interface import CRUD
from database.service import get_db_service
from todo.utils import build_data_model

logger = logging.getLogger(__name__)


class TodoService(CRUD):
    def __init__(self):
        self.db_client = get_db_service()
        
    async def create(self, title: str, content: Optional[str] = "No description...", status: Optional[str] = "To do"):
        """
        Create a todo and add it to the database.
        
        Args:
            title (str): Todo title.
            content (str): Optional longer description (Defaults to "No description").
            status (str): Status (defaults to "To do").
        """
        try:
            data = await build_data_model(title, content, status)
            inserted_data = await self.db_client.insert(type="todo", data=data)
            logger.info(f"Successfully inserted data: {inserted_data}")
        except Exception as e:
            logger.error(f"Error when creating todo: {str(e)}")
        return inserted_data
        
    async def get(self, id: int, fields: Optional[str] = "*"):
        """
        Get todo contents from the database.
        
        Args:
            id (int): Todo row id.
            fields (str): Field values to select from row (Defaults *).
        """
        try:
            todo_content = await self.db_client.select(id=id, type="todo", fields=fields)
            logger.info(f"Successfully read data: {todo_content}")
        except Exception as e:
            logger.error(f"Error when reading todo {e}")
        return todo_content
          
    async def update(
        self, 
        id: int, 
        field: str,
        new_value: str 
    ):
        """
        Update a todo entry in the database.
        
        Args:
            id (int): Todo row id.
            field (str): Field to update.
            new_value (str): Updated field value.
        """
        try:
            updated_data = await self.db_client.update(id=id, type="todo", field=field, value=new_value)
            logger.info(f"Successfully updated data: {updated_data}")
        except Exception as e:
            logger.error(f"Error when reading todo {e}")
        return updated_data
    
    async def delete(self, id):
        """
        Delete a todo from the database.
        
        Args:
            id (int): Todo row id.
        """
        try:
            deleted_data = await self.db_client.delete(id=id, type="todo")
            logger.info(f"Successfully updated data: {deleted_data}")
        except Exception as e:
            logger.error(f"Error when reading todo {e}")
        return deleted_data
    
    
@lru_cache
def get_todo_service():
    return TodoService()