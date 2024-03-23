from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud
from ..schemas import PostCreate, Post, PostUpdate
from ..database import get_db
from ..utils import get_current_sub

router = APIRouter()

@router.post("/", response_model=Post)
def create_post(post: PostCreate, db: Session = Depends(get_db), author_id: int = Depends(get_current_sub)):
    return crud.create_post(db=db, post=post, author_id=author_id)


@router.get("/", response_model=List[Post])
def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_posts(db, skip=skip, limit=limit)
 
@router.get("/{post_id}", response_model=Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.put("/{post_id}", response_model=Post)
def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db), current_id: int = Depends(get_current_sub)):
    db_post = crud.get_post(db, post_id=post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.author_id != current_id:
        raise HTTPException(status_code=403, detail="Not authorized to update this post")
    return crud.update_post(db=db, post_id=post_id, post=post)

@router.delete("/{post_id}", response_model=Post)
def delete_post(post_id: int, db: Session = Depends(get_db),  current_id: int = Depends(get_current_sub)):
    db_post = crud.get_post(db, post_id=post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.author_id != current_id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this post")
    return crud.delete_post(db, post_id=post_id)