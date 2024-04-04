from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from db.database import Base, engine
from routers import post, user

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(post.router)

app.mount("/images", StaticFiles(directory="images"), name="images")
