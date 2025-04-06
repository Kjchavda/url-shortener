from pydantic import BaseModel, HttpUrl

class PostURL(BaseModel):
    url: HttpUrl