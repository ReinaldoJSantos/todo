from sqlalchemy import Column, Integer, String
from app.database.session import Base


class User(Base):
    __table__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hash_password = Column(String, nullable=False)
