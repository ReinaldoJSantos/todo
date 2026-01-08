from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.deps import get_db
from app.schemas.task import TaskCreate, TasksUpdate, TaskResponse
from app.models.task import Task

from app.core.dependecies import get_current_user


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=List[TaskResponse])
def list_task(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user)
              ):
    return db.query(Task).all()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task_id(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    return task


@router.post("/")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = Task(
        title=task.title,
        description=task.description
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


@router.put("/task_id", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TasksUpdate,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada."
        )

    update_data = task_update.dict(exclude_unset=True)

    for field, value in update_data.items():
        setattr(task, field, value)

        db.commit()
        db.refresh(task)

    return task


@router.delete("/{task_id}", status_code=204)
def task_delete(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada.")

    db.delete(task)
    db.commit()
