from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from uuid import UUID

class StaticFileBase(BaseModel):
    storage_backend: str
    direct_url: Optional[str] = None
    filename: Optional[str] = None
    meta_mime: Optional[str] = None
    meta_size: Optional[int] = None
    file_hash: Optional[str] = None

class StaticFileCreate(StaticFileBase):
    id: str

class StaticFileResponse(StaticFileBase):
    id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
