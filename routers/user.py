from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.database import get_db
from repository import user_repository

from . import schema

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.post("", status_code=status.HTTP_201_CREATED)
def create_user(request: schema.UserBase, db: Session = Depends(get_db)):
    return user_repository.create(request, db)
