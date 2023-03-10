from sqlalchemy.orm import Session

import models
import schemas


def get_task(db: Session, task_id: str):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(db: Session, user_id: str, skip: int = 0, limit: int = 100):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).offset(skip).limit(limit).all()


def create_task(db: Session, task: schemas.Task):
    db_task = models.Task(title=task.title, description=task.description, date=task.date, owner_id=task.owner_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: str):
    db.query(models.Task).filter(models.Task.id == task_id).delete()
    db.commit()
