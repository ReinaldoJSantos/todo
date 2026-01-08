from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from app.core.security import SECRETE_KEY, ALGORITHM

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: str = Depends(oauth2_schema)):
    try:
        payload = jwt.decode(token, SECRETE_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")

        if not user_id:
            raise HTTPException(
                status_code=401,
                detail="Tken inválido"
            )

        return user_id
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )