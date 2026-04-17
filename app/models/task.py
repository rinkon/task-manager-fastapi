from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(100))
    is_completed = Column(Boolean)
    due_date = Column(DateTime)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="tasks")
