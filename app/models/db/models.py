from app.core.db import Base
from sqlalchemy import Column, Integer, String, Float, Boolean


class Cars(Base):
    __tablename__ = "cars"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model_name = Column(String)
    year = Column(Integer)
    lat = Column(Float)
    lng = Column(Float)


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
