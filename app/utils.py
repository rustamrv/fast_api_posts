from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import FastAPI, HTTPException, status, Depends
from .security.auth_handler import decodeJWT
from .security.auth_bearer import JWTBearer

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_current_sub(token: str = Depends(JWTBearer())) -> int:
    payload = decodeJWT(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    print(payload)
    user_id: int = payload.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_id
   