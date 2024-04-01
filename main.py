from fastapi import FastAPI

from db.database import Base, engine
from routers import user

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
