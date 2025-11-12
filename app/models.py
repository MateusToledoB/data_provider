from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)


class Numero(Base):
    __tablename__ = "numeros"

    cpf = Column(String(50), primary_key=True, nullable=False)
    numero = Column(String(50), nullable=True)
    email = Column(String(40), nullable=True)