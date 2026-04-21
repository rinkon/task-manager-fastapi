from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, LoginPayload
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.models.user import User
from app.core import hashing
from app.core import security
from app.api import deps
from app.services import auth_service

router = APIRouter()


@router.post('/register', status_code=201)
def register(new_user: UserCreate, db: Session = Depends(get_db)):
    return auth_service.register(new_user, db)

    
@router.post('/login')
def login(payload: LoginPayload, db: Session = Depends(get_db)):
    return auth_service.login(payload.email, payload.password, db)

    

