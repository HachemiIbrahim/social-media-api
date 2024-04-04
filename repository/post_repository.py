from datetime import datetime

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
