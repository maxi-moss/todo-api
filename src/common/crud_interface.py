"""Global interface for todo and notes management services"""

from abc import ABC, abstractmethod
from typing import Optional


class CRUD(ABC):
    @abstractmethod
    async def create(self, title: str, content: Optional[str] = "No description..."):
        """Create a row and insert into the database."""
        pass

    @abstractmethod
    async def get(self, id: int, fields: Optional[str] = "*"):
        """Get contents from a database row."""
        pass

    @abstractmethod
    async def update(self, id: int, field: str, new_value: str):
        """Update a row in the database."""
        pass
    
    @abstractmethod
    async def delete(self, id):
        """Delete a row from the database."""