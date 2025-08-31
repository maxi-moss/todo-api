"""Business logic"""

from typing import Optional
from functools import lru_cache


class TodoService():
    def __init__(self):
        pass
    
    async def create_todo(self, title: str, content: Optional[str] = None, status: Optional[str] = "To do"):
        """
        Create a todo and add it to the database.
        
        Args:
            title (str): Todo title
            content (str): Optional longer description (Defaults to None)
            status (str): Status (defaults to "To do")
        """
        pass
  
    async def read_todo(self, id: int):
        """
        Read contents of a todo from the database.
        
        Args:
            id (int): Todo database id.
        """
        pass
      
    async def update_todo(
        self, 
        id: int, 
        new_title: Optional[str] = None,
        new_content: Optional[str] = None,
        new_status: Optional[str] = None
    ):
        """
        Update a todo entry in the database.
        
        Args:
            id (int): Todo database id.
            new_title (str): Optional updated title.
            new_content (str): Optional updated content.
            new_status (str): Optional updated status.
        """
        pass
    
    async def remove_todo(self, id):
        """
        Remove a todo from the database.
        
        Args:
            id (int): Todo database id.
        """
        pass
    
    
@lru_cache
def get_service():
    return TodoService()