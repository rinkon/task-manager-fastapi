from fastapi import FastAPI
from app.api.routes import auth,tasks
from app.db.base import Base
from app.db.database import engine
from app.models.user import User
from app.models.task import Task

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix='/auth')
app.include_router(tasks.router, prefix='/tasks')
