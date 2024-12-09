# В этом файле описываем само подключение к базе данных
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DB_URL = "sqlite:///./sql_app.db"

engine = create_engine(SQL_DB_URL, connect_args={"check_same_thread": False})  # connect_args = False - убираем
# ограничение на работу из различных потоков

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()