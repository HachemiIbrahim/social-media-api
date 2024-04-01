from sqlalchemy.orm import Session

from db import models
from routers.hashing import Hash
from routers.schema import UserBase


def create(request: UserBase, db: Session):
    new_user = models.User(
        username=request.username,
        email=request.email,
        password=Hash.bycrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
