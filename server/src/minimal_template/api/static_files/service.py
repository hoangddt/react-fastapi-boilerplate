import hashlib
import uuid
from fastapi import UploadFile, HTTPException
from supabase import create_client, Client
from uuid import UUID

from minimal_template.core.config import settings
from minimal_template.api.static_files.repository import StaticFileRepository
from minimal_template.api.static_files.schemas import StaticFileCreate, StaticFileResponse

class StaticFileService:
    def __init__(self):
        # Initialize Supabase client
        supabase_url = settings.SUPABASE_URL
        supabase_key = settings.SUPABASE_KEY
        
        if not supabase_url or not supabase_key:
            raise ValueError("Supabase credentials not found in environment variables")
        
        self.supabase: Client = create_client(supabase_url, supabase_key)
        self.bucket_name = settings.SUPABASE_STORAGE_BUCKET
        self.repository = StaticFileRepository(self.supabase)

    async def upload_file(self, file: UploadFile) -> StaticFileResponse:
        # Read file content
        content = await file.read()
        
        # Calculate file hash
        file_hash = hashlib.sha256(content).hexdigest()
        
        # Generate a unique ID for the file
        file_id = str(uuid.uuid4())
        
        # Upload to Supabase Storage
        file_path = f"{file_id}/{file.filename}"
        try:
            result = self.supabase.storage.from_(self.bucket_name).upload(
                file_path,
                content,
                {"contentType": file.content_type}
            )
            
            # Get the public URL
            public_url = self.supabase.storage.from_(self.bucket_name).get_public_url(file_path)
            
            # Create database entry
            static_file = StaticFileCreate(
                id=file_id,
                storage_backend="supabase",
                direct_url=public_url,
                filename=file.filename,
                meta_mime=file.content_type,
                meta_size=len(content),
                file_hash=file_hash
            )
            
            db_file = self.repository.create(static_file)
            return StaticFileResponse.model_validate(db_file)
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to upload file: {str(e)}")

    def get_file(self, file_id: UUID) -> StaticFileResponse:
        db_file = self.repository.get_by_id(file_id)
        if not db_file:
            raise HTTPException(status_code=404, detail="File not found")
        return StaticFileResponse.model_validate(db_file)
