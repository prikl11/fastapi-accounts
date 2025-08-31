from schemas import UserCreate, UserUpdate, UserOut
from . import SessionDep
from fastapi import APIRouter
from crud import create_user, read_users, update_user, delete_user, read_user

router = APIRouter()

@router.post("/register/user", response_model=UserOut)
def create_user_route(db: SessionDep, user: UserCreate):
    return create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=UserOut)
def read_user_route(db: SessionDep, user_id: int):
    return read_user(db=db, user_id=user_id)

@router.get("/users", response_model=list[UserOut])
def read_users_route(db: SessionDep):
    return read_users(db=db)

@router.patch("/users/{user_id}", response_model=UserOut)
def update_user_route(db: SessionDep, user_id: int, user: UserUpdate):
    return update_user(db=db, user_id=user_id, user=user)

@router.delete("/users/{user_id}")
def delete_user_route(db: SessionDep, user_id: int):
    return delete_user(db=db, user_id=user_id)