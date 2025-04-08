from fastapi import Depends, FastAPI, HTTPException, Response, status
import psycopg2
from psycopg2.extras import RealDictCursor
from app import crud , models
from app.database import engine, get_db



app = FastAPI()

app.include_router(crud.crud_router)

models.Base.metadata.create_all(bind=engine)

try:
    conn = psycopg2.connect(host="localhost", database="Learn_FastAPI", user="postgres", password="kj0910", cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("success")

except Exception as error:
    print("failed")
    print("Error:" , error)

@app.get("/")
def root():
    return {"Welcome": "Root page"}