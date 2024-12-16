from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    role = Column(String)
    login = Column(String, index=True, unique=True)
    password = Column(String)

    # связь с учителем и студентом (необязательно, но можно)
    teacher = relationship("TeachersDB", back_populates="user", uselist=False)
    student = relationship("StudentsDB", back_populates="user", uselist=False)


class StudentsDB(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    teacher_login = Column(String, ForeignKey("teachers.teacher_login"), index=True)
    ready_lessons = Column(JSON)

    user = relationship("Users", back_populates="student")
    teacher = relationship("TeachersDB", back_populates="students_rel")


class TeachersDB(Base):
    __tablename__ = "teachers"

    teacher_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    teacher_login = Column(String, ForeignKey("users.login"), index=True)
    students = Column(JSON)

    user = relationship("Users", back_populates="teacher")
    students_rel = relationship("StudentsDB", back_populates="teacher")
