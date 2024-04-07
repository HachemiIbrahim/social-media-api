from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db import models
from routers.schema import PostBase


def create(request: PostBase, db: Session):
    new_post = models.Post(
        image_url=request.image_url,
        image_url_type=request.image_url_type,
        caption=request.caption,
        timestamp=datetime.now(),
        user_id=request.creator_id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session):
    return db.query(models.Post).all()


def delletPost(db: Session, id: int, user_id: int):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"there is no post with the id {id}",
        )
    if user_id != post.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only post creators can delete there posts",
        )

    db.delete(post)
    db.commit()
    return "OK"
