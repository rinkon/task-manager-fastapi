from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class TaskCreate(BaseModel):
    name: str
    description: str
    is_completed: bool
    due_date: datetime

class TaskRead(BaseModel):
    id: int
    name: str
    description: str
    is_completed: bool
    due_date: datetime

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = None
    due_date: Optional[datetime] = None

    class Config:
        extra = "forbid"

class PaginatedTaskRead(BaseModel):
    tasks: List[TaskRead]
    has_next: bool
