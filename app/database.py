# app/database.py
# Database configuration and session management

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()  # Carrega variaveis do .env (dev local)

DB_USER = os.getenv("USER_NAME") or os.getenv("DB_USER")
DB_PASSWORD = os.getenv("PASSWORD") or os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("HOST") or os.getenv("DB_HOST")
DB_PORT = os.getenv("PORT") or os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

missing = [
    name
    for name, value in {
        "USER_NAME/DB_USER": DB_USER,
        "PASSWORD/DB_PASSWORD": DB_PASSWORD,
        "HOST/DB_HOST": DB_HOST,
        "PORT/DB_PORT": DB_PORT,
        "DB_NAME": DB_NAME,
    }.items()
    if not value
]

if missing:
    raise RuntimeError(
        "Missing required environment variables: " + ", ".join(missing)
    )

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
