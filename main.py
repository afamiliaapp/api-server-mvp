from fastapi import FastAPI

from app.database.connection import engine
from app.database.base import Base

from app.routers import user_router
from app.routers import auth_router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router.router)
app.include_router(user_router.router)