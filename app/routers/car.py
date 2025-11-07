from typing import Annotated
from fastapi import APIRouter, Depends
from app.core.db import SessionLocal
from app.models.db.models import Cars
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/car",
    tags=["car"]
)

db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/get_cars")
async def get_cars(db: db_dependency):
    return db.query(Cars).all()    
