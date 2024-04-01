from fastapi import FastAPI

from db.database import Base, engine
from routers import post, user

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(post.router)
