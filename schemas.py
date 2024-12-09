# В этом файле описываем схемы данных
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    surname: str
    role: str
    login: str
    password: str


class User(UserBase):
    id: int
    ready_lessons: dict

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserInfo(BaseModel):
    name: str
    surname: str
    role: str
    login: str
    ready_lessons: dict
