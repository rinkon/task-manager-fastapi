from app.schemas.user import UserCreate
from fastapi import Depends, HTTPException
from app.db.database import get_db
from app.models.user import User
from app.core import hashing
from sqlalchemy.orm import Session
from app.core import security

def register(new_user: UserCreate, db: Session):
    db_user = db.query(User).filter(User.email == new_user.email).first()

    if db_user:
        raise HTTPException(status_code=409, detail="User already exists")

    hashed_pw = hashing.hash_password(new_user.password)

    db_user = User(
        **new_user.model_dump(exclude={"password"}),
        hashed_password=hashed_pw
    )
    db.add(db_user)
    db.commit()
    
    return {"message": "Registration Successful"}


def login(email: str, password: str, db: Session):
    db_user = db.query(User).filter(User.email == email).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="Invalid Credential")

    if not hashing.verify_hash(password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid Credential")

    token = security.create_token({
        "sub": str(db_user.id),
        "role": db_user.role
    })

    return {
        "access_token": token,
        "type": "bearer"
    }

