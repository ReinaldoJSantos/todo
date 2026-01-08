from fastapi import FastAPI
from app.routes import tasks


app = FastAPI(
    title="API de Tarefas",
    description="Projeto didático com FastAPI e JWT",
    version="1.0.0"
)

app.include_router(tasks.router)


@app.get("/healt")
def get_healt():
    return {"message": "Ok"}