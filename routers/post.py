import random
import shutil
import string
from typing import List

from fastapi import APIRouter, Depends, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db.database import get_db
from repository import post_repository
from routers.schema import UserAuth

from . import schema

router = APIRouter(
    prefix="/post",
    tags=["post"],
)

image_url_types = ["relative", "absolute"]
# absolute : from web
# relative : from the device


@router.post("", status_code=status.HTTP_201_CREATED, response_model=schema.PostDisplay)
def create_post(
    request: schema.PostBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    if request.image_url_type not in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)
    return post_repository.create(request, db)


@router.get("/all", response_model=List[schema.PostDisplay])
def get_all_posts(db: Session = Depends(get_db)):
    return post_repository.get_all(db)


@router.post("/images")
def upload_image(image: UploadFile, current_user: UserAuth = Depends(get_current_user)):
    letters = string.ascii_letters
    random_string = "".join(random.choice(letters) for i in range(6))
    new = f"_{random_string}."
    filename = new.join(image.filename.rsplit(".", 1))
    path = f"images/{filename}"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {"filename": path}
