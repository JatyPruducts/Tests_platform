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

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class UserInfo(BaseModel):
    id: int
    name: str
    surname: str
    role: str
    login: str


#################################

class StudentBase(BaseModel):
    user_id: int
    teacher_login: str


class Student(StudentBase):
    student_id: int
    ready_lessons: dict

    class Config:
        orm_mode = True


class StudentCreate(StudentBase):
    pass


##################################

class TeacherBase(BaseModel):
    user_id: int
    teacher_login: str


class TeacherCreate(TeacherBase):
    pass


class Teacher(TeacherBase):
    teacher_id: int
    students: dict

    class Config:
        orm_mode = True
