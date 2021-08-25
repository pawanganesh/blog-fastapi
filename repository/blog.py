from sqlalchemy.orm import Session
from .. import models


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs
