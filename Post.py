from datetime import datetime
from typing import Optional, List, Dict

class Post:
    def __init__(self, data: Dict):
        self.id: int = data.get("id")
        self.created_at: datetime = datetime.fromisoformat(data.get("created_at"))
        self.updated_at: datetime = datetime.fromisoformat(data.get("updated_at"))
        
        self.file: Dict = data.get("file", {})
        self.preview: Dict = data.get("preview", {})
        self.sample: Dict = data.get("sample", {})
        
        self.score: Dict = data.get("score", {})
        
        self.tags: Dict = data.get("tags", {})
        self.locked_tags: List[str] = data.get("locked_tags", [])
        
        self.change_seq: int = data.get("change_seq")
        self.flags: Dict = data.get("flags", {})
        self.rating: str = data.get("rating")
        self.fav_count: int = data.get("fav_count")
        self.sources: List[str] = data.get("sources", [])
        self.pools: List[str] = data.get("pools", [])
        
        self.relationships: Dict = data.get("relationships", {})
        self.approver_id: Optional[int] = data.get("approver_id")
        self.uploader_id: Optional[int] = data.get("uploader_id")
        
        self.description: str = data.get("description")
        self.comment_count: int = data.get("comment_count")
        self.is_favorited: bool = data.get("is_favorited")
        self.has_notes: bool = data.get("has_notes")
        self.duration: Optional[int] = data.get("duration")

