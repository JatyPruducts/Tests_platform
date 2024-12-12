from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import bcrypt

from fastapi.middleware.cors import CORSMiddleware
from models import Base, Users, StudentsDB, TeachersDB
from database import engine, session_local
from schemas import UserCreate, User, UserInfo, Student, StudentCreate, Teacher, TeacherCreate


async def hash_password(password):
    # Генерация соли
    salt = bcrypt.gensalt()
    # Хэширование пароля с солью
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


async def check_password(stored_password: str, provided_password: str) -> bool:
    # Проверка введенного пароля с сохраненным хэшем
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))


# uvicorn main:app --reload
app = FastAPI()

origins = [  # указываем допустимые источники запросов
    "http://localhost:8080",
    "http://127.0.0.1:8080"
]

app.add_middleware(  # указываем промежуточное ПО
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


def get_db():
    db = session_local()
    try:
        yield db  # yield - конструкция, которая возвращает сессию
        # базы данных для дальнейшего использования в маршрутах.
    finally:
        db.close()


async def add_student_to_teacher(teacher, student: Student, db: Session = Depends(get_db)):
    teacher_db = db.query(TeachersDB).filter(TeachersDB.teacher_login == teacher.teacher_login).first()
    teacher_db.students[int(student.student_id)] = student.ready_lessons
    db.merge(teacher_db)
    db.add(teacher_db)
    db.commit()

@app.post("/user/create/", response_model=User)  # модель возвращаемого ответа
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    existing_user = db.query(Users).filter(Users.login == user.login).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    db_user = Users(
        name=user.name,
        surname=user.surname,
        role=user.role,
        login=user.login,
        password=await hash_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/user/user_info={user_id}", response_model=UserInfo)  # модель возвращаемого ответа
async def get_info_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/user/login/", response_model=UserInfo)
async def login_user(user_login: str, user_password: str, db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.login == user_login).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if not await check_password(db_user.password, user_password):
        raise HTTPException(status_code=401, detail="Invalid password")
    return db_user


@app.post("/student/create/", response_model=Student)  # модель возвращаемого ответа
async def create_student(student: StudentCreate, db: Session = Depends(get_db)):

    teacher = db.query(TeachersDB).filter(TeachersDB.teacher_login == student.teacher_login).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail="Такой учитель не найден")

    student_id = db.query(StudentsDB).filter(StudentsDB.user_id == student.user_id).first()
    if student_id is not None:
        raise HTTPException(status_code=400, detail="Students already exists")

    new_student = StudentsDB(
        user_id=student.user_id,
        teacher_login=student.teacher_login,
        ready_lessons={}
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    await add_student_to_teacher(teacher, new_student, db)
    return new_student


@app.post("/teacher/create/", response_model=Teacher)
async def create_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    teacher_db = db.query(TeachersDB).filter(TeachersDB.teacher_login == teacher.teacher_login).first()
    if teacher_db is not None:
        raise HTTPException(status_code=400, detail="Такой учитель уже создан")
    new_teacher = TeachersDB(
        user_id=teacher.user_id,
        teacher_login=teacher.teacher_login,
        students={}
    )
    db.add(new_teacher)

    db.commit()
    db.refresh(new_teacher)
    return new_teacher


@app.get("/teacher/teacher_login={teacher_login}/all_students/")
async def all_students(teacher_login: str, db: Session = Depends(get_db)):
    teacher = db.query(TeachersDB).filter(TeachersDB.teacher_login == teacher_login).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail="Такой учитель не найден")
    return teacher.students
