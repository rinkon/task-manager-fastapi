from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.tasks import TaskCreate, TaskUpdate


def create_task(task: TaskCreate, user_id: int, db: Session):
    
    db_task = Task(
        **task.model_dump(),
        owner_id=user_id
    )
    db.add(db_task)
    db.commit()

    return {"message": "Task creation successful"}


def get_user_tasks(user_id: int, db: Session):
    db_tasks = db.query(Task).filter(Task.owner_id == user_id).all()
    return db_tasks


def get_task_by_id(task_id: int, user_id: int, db: Session):
    db_task = db.query(Task).filter(Task.id == task_id).first()

    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if db_task.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden access")
    
    return db_task


def update_task_by_id(task: TaskUpdate, task_id: int, user_id: int, db: Session):
    
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if db_task.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden access")

    update_data = task.model_dump(exclude_unset=True)
    if not update_data:
        return {"message": "No changes provided"}
    
    for key, value in task.model_dump(exclude_unset=True).items():
        setattr(db_task, key, value)
    
    db.commit()
    db.refresh(db_task)

    return {"message": "Task update successful"}


def delete_task_by_id(task_id: int, user_id: int, db: Session):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_task.owner_id != user_id:
        raise HTTPException(status_code=403, detail="Forbidden access")
    db.delete(db_task)
    db.commit()
    return {"message": "Task deletion successful"}
