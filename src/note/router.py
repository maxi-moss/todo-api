"""API routes / endpoints"""


from fastapi import APIRouter, Depends

from note.schemas import NoteCreateRequest, NoteDeleteRequest, NoteUpdateRequest
from note.service import NoteService, get_note_service

router = APIRouter()


@router.post("/create")
async def create(
    request: NoteCreateRequest,
    service: NoteService = Depends(get_note_service)
):
    results = await service.create(
        request.title,
        request.content
    )
    return {"message": f"Successfully created note: {results}"}


@router.get("/get")
async def get(
    id: int,
    fields: str,
    service: NoteService = Depends(get_note_service),
):
    """
    Get field values by row id and type.
    
    Args:
        id (int): Entry id.
        fields (str): Fields to select (Example: "title, content").
    """
    fetched_data = await service.get(
        id,
        fields
    )
    return {"message": f"Successfully fetched data from note {id}: {fetched_data}"}


@router.post("/update")
async def update(
    request: NoteUpdateRequest,
    service: NoteService = Depends(get_note_service)
):
    """
    Update a note entry in the database.
    
    Args:
        id (int): Note row id.
        field (str): Field to update.
        new_value (str): Updated field value.
    """
    updated_data = await service.update(
        request.id,
        request.field,
        request.new_value
    )
    return {"message": f"Successfully updated data of note {request.id}: {updated_data}"}


@router.post("/delete")
async def delete(
    request: NoteDeleteRequest,
    service: NoteService = Depends(get_note_service)
):
    deleted_data = await service.delete(
        request.id
    )
    return {"message": f"Successfully deleted note {request.id}: {deleted_data}"}