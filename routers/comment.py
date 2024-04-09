from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.oauth2 import get_current_user
from db.database import get_db
from repository import comment_repository
from routers.schema import UserAuth

from . import schema

router = APIRouter(
    prefix="/comment",
    tags=["comment"],
)


@router.get("/all/{post_id}")
def get_all(post_id: int, db: Session = Depends(get_db)):
    return comment_repository.get_all(db, post_id)


@router.post("")
def create(
    request: schema.CommentBase,
    db: Session = Depends(get_db),
    current_user: UserAuth = Depends(get_current_user),
):
    return comment_repository.create(db, request)
