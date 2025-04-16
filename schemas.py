from typing import Optional, List
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    surname: str
    role: str
    login: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserAuth(BaseModel):
    login: str
    password: str


class StudentBase(BaseModel):
    user_id: int
    teacher_login: str
    ready_lessons: Optional[List[dict]] = []


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    student_id: int

    class Config:
        orm_mode = True


class TeacherBase(BaseModel):
    user_id: int
    teacher_login: str


class TeacherCreate(TeacherBase):
    pass


class Teacher(TeacherBase):
    teacher_id: int

    class Config:
        orm_mode = True


class TestBase(BaseModel):
    test_name: str


class TestCreate(TestBase):
    test_id: int

    class Config:
        orm_mode = True


class UserResults(BaseModel):
    user_login: str
    test_name: str
    result: int
