from datetime import datetime
from typing import List


from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str  # hash password


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: int


# for PostDisplay
class User(BaseModel):
    username: str

    class Config:
        orm_mode = True


class Comment(BaseModel):
    username: str
    text: str
    timestamp: datetime

    class Config:
        orm_mode = True


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: List[Comment]

    class Config:
        orm_mode = True


class UserAuth(BaseModel):
    id: int
    username: str
    email: str


class CommentBase(BaseModel):
    username: str
    text: str
    post_id: int
