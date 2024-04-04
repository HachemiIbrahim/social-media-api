from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.database import get_db
from repository import post_repository

from . import schema

router = APIRouter(
    prefix="/post",
    tags=["post"],
)

image_url_types = ["relative", "absolute"]
# absolute : from web
# relative : from the device


@router.post("", status_code=status.HTTP_201_CREATED, response_model=schema.PostDisplay)
def create_post(request: schema.PostBase, db: Session = Depends(get_db)):
    if request.image_url_type not in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return post_repository.create(request, db)


@router.get("", response_model=List[schema.PostDisplay])
def get_all_posts(db: Session = Depends(get_db)):
    return post_repository.get_all(db)
