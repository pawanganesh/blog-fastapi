from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

import database
import schemas
from repository import blog as rep_blog

get_db = database.get_db

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)


@router.get("/", response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return rep_blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(blog: schemas.Blog, db: Session = Depends(get_db)):
    return rep_blog.create(blog, db)


@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db)):
    return rep_blog.show(id, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    return rep_blog.destroy(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id, blog: schemas.Blog, db: Session = Depends(get_db)):
    return rep_blog.update(id, blog, db)
