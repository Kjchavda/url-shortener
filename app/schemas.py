from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional

class PostURL(BaseModel):
    original_url: HttpUrl

class URLInfo(BaseModel):
    id: int
    short_url: str
    original_url: HttpUrl
    # clicks: int
    created_at: datetime

    class Config:
        orm_mode = True


class URLUpdate(BaseModel):
    original_url: Optional[HttpUrl] = None  # Optional in case partial update
