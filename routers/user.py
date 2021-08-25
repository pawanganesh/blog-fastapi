from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import database
import schemas
from repository import user as userRepository

get_db = database.get_db

router = APIRouter(
    prefix="/user",
    tags=['users']
)


@router.post("/", response_model=schemas.ShowUser)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return userRepository.create(user, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return userRepository.show(id, db)
