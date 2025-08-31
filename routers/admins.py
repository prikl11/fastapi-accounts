from . import SessionDep
from fastapi import APIRouter
from crud import create_admin, read_admin, read_admins, update_admin, delete_admin
from schemas import AdminCreate, AdminOut, AdminUpdate

router = APIRouter()

@router.post("/register/admin", response_model=AdminOut)
def create_admin_route(db: SessionDep, admin: AdminCreate):
    return create_admin(db=db, admin=admin)

@router.get("/admins", response_model=list[AdminOut])
def read_admins_route(db: SessionDep):
    return read_admins(db=db)

@router.get("/admins/{admin_id}", response_model=AdminOut)
def read_admin_route(db: SessionDep, admin_id: int):
    return read_admin(db=db, admin_id=admin_id)

@router.patch("/admins/{admin_id}", response_model=AdminOut)
def update_admin_route(db: SessionDep, admin_id: int, admin: AdminUpdate):
     return update_admin(db=db, admin_id=admin_id, admin=admin)

@router.delete("/admins/{admin_id}")
def delete_admin_route(db: SessionDep, admin_id: int):
    return delete_admin(db=db, admin_id=admin_id)