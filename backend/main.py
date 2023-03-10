from fastapi import FastAPI, Response, Depends, Cookie, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from sqlalchemy.orm import Session
import uvicorn

import crud
import models
import schemas

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_user_id(response: Response, user_id: str | None = Cookie(default=None)):
    if user_id is None:
        user_id = os.urandom(16).hex()
        response.set_cookie(key="user_id", value=user_id)
    return user_id


@app.get("/")
async def root():
    return {'message': 'OK'}


@app.get("/tasks", response_model=list[schemas.Task])
async def read_tasks(user_id: str = Depends(get_user_id), db: Session = Depends(get_db)):
    return crud.get_tasks(db, user_id)


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str, db: Session = Depends(get_db), user_id: str = Depends(get_user_id)):
    task = crud.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.owner_id != user_id:
        raise HTTPException(status_code=403, detail="You don't have permission to delete this task")
    crud.delete_task(db, task_id)
    return {"message": "success!", "id": task_id}


@app.post("/tasks", response_model=schemas.Task)
async def create_task(
    task: schemas.TaskBase, db: Session = Depends(get_db), user_id: str = Depends(get_user_id)
):
    task_full = schemas.Task
    task_full.title = task.title
    task_full.description = task.description
    task_full.date = task.date
    task_full.owner_id = user_id
    return crud.create_task(db=db, task=task_full)


if __name__ == '__main__':
    uvicorn.run("main:app", port=85, host='localhost', reload=True)
