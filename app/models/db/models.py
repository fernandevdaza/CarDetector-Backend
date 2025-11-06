from app.core.db import Base
from sqlalchemy import Column, Integer, String, Float

class Cars(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model_name = Column(String)
    year = Column(Integer)
    lat = Column(Float)
    lng = Column(Float)