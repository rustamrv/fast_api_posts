from fastapi import FastAPI, HTTPException, status

from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db
from datetime import datetime, timedelta
from ..security import sign_jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 30


def signup(user: schemas.UserCreate, db: Session = next(get_db())):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = utils.hash_password(user.password)
    db_user = models.User(email=user.email, password=hashed_password, first_name=user.first_name, last_name=user.last_name)
    db.add(db_user)
    db.commit()
    return sign_jwt(db_user.id)

def get_user_by_email(email: str,  db: Session = next(get_db())):
    return db.query(models.User).filter(models.User.email == email).first()

def authenticate_user(email: str, password: str, db: Session = next(get_db())):
    user = get_user_by_email(email, db)
    if not user or not utils.verify_password(password, user.password):
        return False
    return user


def login(user: schemas.LoginCreate, db: Session = next(get_db())):
    user = authenticate_user(user.email, user.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        ) 
    return sign_jwt(user.id)