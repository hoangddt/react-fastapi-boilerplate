from uuid import UUID
from supabase import Client

from minimal_template.api.static_files.schemas import StaticFileCreate

class StaticFileRepository:
    def __init__(self, supabase: Client):
        self.supabase = supabase
        self.table_name = "tl__static_file"

    def create(self, static_file: StaticFileCreate) -> dict:
        data = static_file.model_dump()
        result = self.supabase.table(self.table_name).insert(data).execute()
        
        if not result.data or len(result.data) == 0:
            raise Exception("Failed to create static file record")
            
        return result.data[0]

    def get_by_id(self, file_id: UUID) -> dict | None:
        result = self.supabase.table(self.table_name).select("*").eq("id", str(file_id)).execute()
        
        if not result.data or len(result.data) == 0:
            return None
            
        return result.data[0]
