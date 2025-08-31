from datetime import datetime
import asyncio
import logging

from supabase import create_client
import supabase

from config import settings

logger = logging.getLogger(__name__)


class DatabaseService():
    def __init__(self):
        self.client = create_client(
            supabase_url=settings.supabase.url,
            supabase_key=settings.supabase.key
        )
    
    async def select_table(self, type: str):
        """
        Get table contents based on type.
        
        Args:
            type (str): Type of entry ("todo" or "note").
        """
        response = (
            self.client.table(type)
            .select("*")
            .execute()
        )
        return response

    async def select(self, id: int, fields: str = "*", type: str = "todo"):
        """
        Get field values by row id and type.
        
        Args:
            id (int): Entry id.
            fields (str): Fields to select (Example: "title, content").
            type (str): Type of entry ("todo" or "note").    
        """
        response = (
            self.client.table(type)
            .select(fields)
            .eq("id", id)
            .execute()
        )
        return response
    
    async def insert(self, data, type: str = "todo"):
        """
        Insert a new row into database.
        
        Args:
            id (int): Database row id.
            data (str): Column data to insert.
            type (str): Type of entry ("todo" or "note").    
        """
        response = (
            self.client.table(type)
            .insert(data)
            .execute()
        )
        return response
    
    async def update(self, id: int, field: str, value: str, edit_time, type: str):
        """
        Update a field for a given database row.
        
        Args:
            id (int): Database row id.
            fields (str): Fields to select (Example: "title, content").
            type (str): Type of entry ("todo" or "note").    
        """
        response = (
            self.client.table(type)
            .update({field: value, "edited_at": edit_time})
            .eq("id", id)
            .execute()
        )
        return response
        
    async def delete(self, id: int, type: str):
        """
        Delete a row from the database.
        
        Args:
            id (int): Database row id.
            type (str): Type of entry ("todo" or "note").    
        """
        response = (
            self.client.table(type)
            .select("title, content")
            .eq("id", id)
            .execute()
        )
        return response
    

Database = DatabaseService()
current_time = str(datetime.now())

# --- Insert test ---
#data = {"title": "test the app", "content": "This is a test", "created_at": current_time, "edited_at": current_time, "status": "in_progress"}
#response = asyncio.run(Database.insert(data=data, type="todo"))

# --- Update test ---
#response = asyncio.run(Database.update(id=4, field="title", value="gay", edit_time=current_time, type="todo"))

# --- Delete test ---
#response = asyncio.run(Database.delete(id=1, type="todo"))

# --- Select test ---
response = asyncio.run(Database.select(id=3, fields="title, content", type="todo"))

# --- Print test results ---
print(response)