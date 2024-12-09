from fastapi import FastAPI, HTTPException, Path, Query, Body, Depends
from sqlalchemy.orm import Session
import bcrypt

from fastapi.middleware.cors import CORSMiddleware
from models import Base, Users
from database import engine, session_local
from schemas import UserCreate, User


def hash_password(password):
    # Генерация соли
    salt = bcrypt.gensalt()
    # Хэширование пароля с солью
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def check_password(stored_password: str, provided_password: str) -> bool:
    # Проверка введенного пароля с сохраненным хэшем
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))


# uvicorn main:app --reload
app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db  # yield - конструкция, которая возвращает сессию
        # базы данных для дальнейшего использования в маршрутах.
    finally:
        db.close()


@app.post("/create_user/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> Users | str:
    db_user = Users(
        name=user.name,
        surname=user.surname,
        role=user.role,
        login=user.login,
        password=hash_password(user.password),
        ready_lessons={}
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


