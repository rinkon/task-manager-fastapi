from sqlalchemy import Column, Integer, String
from app.db.base import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    role = Column(String(100), nullable=False)
    hashed_password = Column(String(100), nullable=False)
    tasks = relationship("Task", back_populates="owner")
