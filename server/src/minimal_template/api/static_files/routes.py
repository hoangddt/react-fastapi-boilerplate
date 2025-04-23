from fastapi import APIRouter, Depends, UploadFile, File
from uuid import UUID

from minimal_template.api.static_files.service import StaticFileService
from minimal_template.api.static_files.schemas import StaticFileResponse

router = APIRouter(prefix="/static-files", tags=["static-files"])

def get_static_file_service() -> StaticFileService:
    return StaticFileService()

@router.post("/upload", response_model=StaticFileResponse)
async def upload_file(
    file: UploadFile = File(...),
    service: StaticFileService = Depends(get_static_file_service)
) -> StaticFileResponse:
    """
    Upload a static file to Supabase storage and create a database entry.
    """
    return await service.upload_file(file)

@router.get("/{file_id}", response_model=StaticFileResponse)
def get_file(
    file_id: UUID,
    service: StaticFileService = Depends(get_static_file_service)
) -> StaticFileResponse:
    """
    Get file information by ID.
    """
    return service.get_file(file_id)
