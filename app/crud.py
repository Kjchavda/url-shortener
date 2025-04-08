from fastapi import Depends, FastAPI, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session
from app import schemas
from app.utils import generate_short_code, is_unique_short_code
from app.database import get_db
from app import models

crud_router = APIRouter(
    tags=['crud']
)

@crud_router.post("/shorten", response_model=schemas.URLInfo, status_code=status.HTTP_201_CREATED)
def shorten(url: schemas.PostURL, db: Session = Depends(get_db)):
    short_code = generate_short_code()
    while not is_unique_short_code(db, short_code=short_code):
        short_code = generate_short_code()
    db_url = models.URL(original_url=str(url.original_url), short_url=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    if db_url == None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bad Request")
    return db_url

@crud_router.get("/shorten/{short_code}",response_model=schemas.URLInfo , status_code=status.HTTP_200_OK)
def get_short_url(short_code: str, db: Session = Depends(get_db)):
    db_url = db.query(models.URL).filter(models.URL.short_url == short_code).first()
    if db_url == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No url found for this short code")
    return db_url

@crud_router.put("/shorten/{short_code}", response_model=schemas.URLInfo, status_code=status.HTTP_200_OK)
def update_url(short_code: str,updated_url: schemas.URLUpdate, db: Session = Depends(get_db)):
    updated_url.original_url = str(updated_url.original_url)
    db_query = db.query(models.URL).filter(models.URL.short_url == short_code)
    db_url = db_query.first()
    if db_url == None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Url with code {short_code} was not found")
    db_query.update(updated_url.model_dump() , synchronize_session = False)
    db.commit()
    return db_url