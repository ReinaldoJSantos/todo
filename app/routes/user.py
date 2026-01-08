from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from app.database.deps import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import hash_password


router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    exists = db.query(User).filter(User.email == user.email).first()

    if exists:
        raise HTTPException(
            status_code=404,
            detail="Email já cadastrado")

    db_user = User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user