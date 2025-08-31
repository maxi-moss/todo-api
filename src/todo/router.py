"""API routes / endpoints"""


from fastapi import APIRouter, Depends

from todo.schemas import TodoCreateRequest, TodoDeleteRequest, TodoUpdateRequest
from todo.service import TodoService, get_todo_service

router = APIRouter()


@router.post("/create")
async def create_todo(
    request: TodoCreateRequest,
    service: TodoService = Depends(get_todo_service)
):
    results = await service.create_todo(
        request.title,
        request.content,
        request.status
    )
    return {"message": f"Successfully created todo: {results}"}


@router.get("/get")
async def get_todo(
    id: int,
    fields: str,
    service: TodoService = Depends(get_todo_service),
):
    """
    Get field values by row id and type.
    
    Args:
        id (int): Entry id.
        fields (str): Fields to select (Example: "title, content").
    """
    fetched_data = await service.get_todo(
        id,
        fields
    )
    return {"message": f"Successfully fetched data from todo {id}: {fetched_data}"}


@router.post("/update")
async def update_todo(
    request: TodoUpdateRequest,
    service: TodoService = Depends(get_todo_service)
):
    """
    Update a todo entry in the database.
    
    Args:
        id (int): Todo row id.
        field (str): Field to update.
        new_value (str): Updated field value.
    """
    updated_data = await service.update_todo(
        request.id,
        request.field,
        request.new_value
    )
    return {"message": f"Successfully updated data of todo {request.id}: {updated_data}"}


@router.post("/delete")
async def delete_todo(
    request: TodoDeleteRequest,
    service: TodoService = Depends(get_todo_service)
):
    deleted_data = await service.delete_todo(
        request.id
    )
    return {"message": f"Successfully deleted todo {request.id}: {deleted_data}"}