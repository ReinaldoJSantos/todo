from fastapi import FastAPI
from app.database.session import Base, engine
from app.models import task
from app.routes import tasks


app = FastAPI(
    title="API de Tarefas",
    description="Projeto didático com FastAPI e JWT",
    version="1.0.0"
)

app.include_router(tasks.router)

Base.metadata.create_all(bind=engine)
