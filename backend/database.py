from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://root:{os.getenv("DBPASS", "rectione")}@{os.getenv("DATABASE", "127.0.0.1")}/todo?charset=utf8mb4'


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
