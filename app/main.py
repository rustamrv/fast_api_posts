from fastapi import APIRouter
from .database import SessionLocal, engine
from .routers import posts, users


api_router = APIRouter()  
 
api_router.include_router(users.router, prefix="/auth", tags=["auth"])
api_router.include_router(posts.router, prefix="/posts", tags=["posts"])