from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    description: str
    date: str


class Task(TaskBase):
    id: int
    owner_id: str

    class Config:
        orm_mode = True
