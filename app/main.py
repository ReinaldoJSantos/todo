from app.core.config import settings
from fastapi import FastAPI
from app.database.session import Base, engine
from app.routes import tasks, users, auth


app = FastAPI(
    title=settings.app_name,
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(tasks.router)
