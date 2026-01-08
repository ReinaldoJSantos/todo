from fastapi import APIRouter, HTTPException
from app.schemas.task import TaskCreate, TasksUpdate


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/{task_id}")
def get_task(task_id: int):
    # Simulando tarefa existente
    fake_task = {
        "id": task_id,
        "title": "Estudar FastAPI",
        "description": "Exerccício bônus",
        "completed": False
    }

    # Simulando validação simpçles
    if task_id <= 0:
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    return fake_task


@router.post("/")
def create_task(task: TaskCreate):
    return {
        "id": 1,
        "completed": False,
        **task.dict()
    }


@router.put("/task_id")
def update_tasks(task_id: int, task: TasksUpdate):
    # Simulanddo uma tarefa existente
    fake_task = {
        "id": task_id,
        "title": "Tarefa antiga",
        "description": "Descrição antiga",
        "completed": False
    }
    update_data = task.dict(exclude_unset=True)
    fake_task.update(update_data)

    return fake_task
