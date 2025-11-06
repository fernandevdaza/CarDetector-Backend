from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "app.db"

SQLALCHEMY_DATABASE_URI = f'sqlite:///{DB_PATH.as_posix()}'

engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={
    'check_same_thread': False
})

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
