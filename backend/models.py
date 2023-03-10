from sqlalchemy import Column, Integer, TEXT
from database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(TEXT)
    description = Column(TEXT)
    date = Column(TEXT)
    owner_id = Column(TEXT)

