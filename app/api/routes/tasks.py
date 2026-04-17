from fastapi import APIRouter, Depends, HTTPException
from app.api import deps
from app.db import database
from sqlalchemy.orm import Session
from app.schemas.tasks import TaskCreate, TaskRead, TaskUpdate
from app.models.task import Task
from app.services import task_service
from typing import List

router = APIRouter()

@router.get('/tasks', response_model=List[TaskRead])
def get_user_tasks(current_user: dict = Depends(deps.get_current_user), db: Session = Depends(database.get_db)):
    user_id = current_user.get('user_id')
    return task_service.get_user_tasks(user_id=user_id, db=db)


@router.post('/tasks')
def create_task(task: TaskCreate, current_user: dict = Depends(deps.get_current_user), db: Session = Depends(database.get_db)):
    user_id = current_user.get('user_id')
    return task_service.create_task(task=task, user_id=user_id, db=db)
    

@router.get('/tasks/{task_id}', response_model=TaskRead)
def get_task_by_id(task_id: int, current_user: dict = Depends(deps.get_current_user), db: Session = Depends(database.get_db)):
    user_id = current_user.get('user_id')
    return task_service.get_task_by_id(task_id=task_id, user_id=user_id, db=db)


@router.patch('/tasks/{task_id}')
def update_task_by_id(task: TaskUpdate, task_id: int, current_user: dict = Depends(deps.get_current_user), db: Session = Depends(database.get_db)):
    user_id = current_user.get('user_id')
    return task_service.update_task_by_id(task=task, task_id=task_id, user_id=user_id, db=db)
    
    

