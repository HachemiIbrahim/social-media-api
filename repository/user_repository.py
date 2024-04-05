from fastapi import HTTPException, status
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


def get_user_by_username(db: Session, username=str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with username {username} not found",
        )
    return user
