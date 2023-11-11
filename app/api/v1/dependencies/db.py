# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

print(f"Database URL: {settings.DATABASE_URL}")  # This is for debugging purposes
engine = create_engine(settings.DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
def init_db():
    Base.metadata.create_all(bind=engine)
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    