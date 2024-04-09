from datetime import datetime

from sqlalchemy.orm import Session

from db import models
from routers.schema import CommentBase


def create(db: Session, request: CommentBase):
    new_comment = models.Comments(
        text=request.text,
        username=request.username,
        post_id=request.post_id,
        timestamp=datetime.now(),
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all(db: Session, post_id: int):
    return db.query(models.Comments).filter(models.Comments.post_id == post_id).all()
