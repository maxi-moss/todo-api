"""Business logic"""

from typing import Optional

from functools import lru_cache


class NoteService():
    def __init__(self):
        pass
    
    async def create_note(self, title: str, content: Optional[str] = None):
        """
        Create a note and add it to the database.
        
        Args:
            title (str): Note title
            content (str): Optional longer description (Defaults to None)
        """
        pass
  
    async def read_note(self, id: int):
        """
        Read contents of a note from the database.
        
        Args:
            id (int): Todo database id.
        """
        pass
      
    async def update_note(
        self, 
        id: int, 
        new_title: Optional[str] = None,
        new_content: Optional[str] = None,
    ):
        """
        Update a todo entry in the database.
        
        Args:
            id (int): Note database id.
            new_title (str): Optional updated title.
            new_content (str): Optional updated content.
        """
        pass
    
    async def remove_note(self, id: int):
        """
        Remove a note from the database.
        
        Args:
            id (int): Note database id.
        """
        pass
    
    
@lru_cache
def get_note_service():
    return NoteService()