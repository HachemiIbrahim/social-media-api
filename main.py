from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from auth import authentication
from db.database import Base, engine
from routers import comment, post, user

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(comment.router)
app.include_router(post.router)

app.mount("/images", StaticFiles(directory="images"), name="images")
