from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from db.schemas import UserBase, UserDisplay
from db import db_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)


# Create user
@router.post('/new', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


# Read all users
@router.get('/all', response_model=list[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


# Read one user by id
@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, id)


# Update user
@router.post('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, id, request)


# Delete user
@router.get('/{id}/delete')
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)
