from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    role: str
    password: str


class UserRead(BaseModel):
    name: str
    email: str
    role: str


class LoginPayload(BaseModel):
    email: str
    password: str
