# в этом файле описываем каждую табличку в базе данных
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    surname = Column(String, index=True)
    role = Column(String, index=True)
    login = Column(String, index=True, unique=True)
    password = Column(String)
    ready_lessons = Column(JSON)


class StudentsDB(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    teacher_login = Column(String, ForeignKey("users.login"), index=True)


