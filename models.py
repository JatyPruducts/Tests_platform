from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    role = Column(String)
    login = Column(String, index=True, unique=True)
    password = Column(String)


class StudentsDB(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    teacher_login = Column(String, ForeignKey("teachers.teacher_login"), index=True)
    ready_lessons = Column(JSON)


class TeachersDB(Base):
    __tablename__ = "teachers"

    teacher_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    teacher_login = Column(String, ForeignKey("users.login"), index=True)


class TestsDB(Base):
    __tablename__ = "tests"

    test_id = Column(Integer, primary_key=True, index=True)
    test_name = Column(String, index=True)
