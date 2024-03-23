from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud
from ..schemas import UserCreate, LoginCreate, TokenResponse
from ..database import get_db

router = APIRouter()

@router.post("/sign_up", response_model=TokenResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return crud.signup(user=user, db=db)

@router.post("/sign_in", response_model=TokenResponse)
def login(user: LoginCreate, db: Session = Depends(get_db)):
    return crud.login(user=user, db=db)

 
