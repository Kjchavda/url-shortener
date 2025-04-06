from fastapi import Depends, FastAPI, HTTPException, Response, status, APIRouter
from app import schemas
from .utils import generate_short_code

crud_router = APIRouter(
    tags=['crud']
)

@crud_router.post("/shorten")
def shorten(url: schemas.PostURL):
    short_url = generate_short_code()
    return {"Short" : short_url}