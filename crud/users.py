from fastapi import HTTPException
from schemas import UserCreate, UserUpdate
from models import Users
from sqlalchemy.orm import Session
from security import hash_password

def create_user(db: Session, user: UserCreate):
    existing_user = db.query(Users).filter(Users.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = Users(email=user.email, full_name=user.full_name, hashed_password=hash_password(user.hashed_password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def read_user(db: Session, user_id: int):
    user = db.query(Users).filter(Users.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

def read_users(db: Session):
    return db.query(Users).all()

def update_user(db: Session, user_id: int, user: UserUpdate):
    existing_user = db.query(Users).filter(Users.id == user_id).first()
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.email is not None:
        existing_user.email = user.email
    if user.hashed_password is not None:
        existing_user.hashed_password = hash_password(user.hashed_password)
    if user.full_name is not None:
        existing_user.full_name = user.full_name

    db.commit()
    db.refresh(existing_user)
    return existing_user

def delete_user(db: Session, user_id: int):
    user = db.query(Users).filter(Users.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted"}