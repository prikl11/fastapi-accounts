from fastapi import HTTPException
from schemas import AdminCreate, AdminUpdate
from models import Admin
from sqlalchemy.orm import Session
from security import hash_password

def create_admin(db: Session, admin: AdminCreate):
    existing_admin = db.query(Admin).filter(Admin.email == admin.email).first()
    if existing_admin:
        raise HTTPException(status_code=400, detail="Admin already exists")

    new_admin = Admin(user_id=admin.user_id, email=admin.email, full_name=admin.full_name, hashed_password=hash_password(admin.hashed_password))
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin

def read_admin(db: Session, admin_id: int):
    admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    return admin

def read_admins(db: Session):
    return db.query(Admin).all()

def update_admin(db: Session, admin_id: int, admin: AdminUpdate):
    existing_admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if not existing_admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    if admin.user_id is not None:
        existing_admin.user_id = admin.user_id
    if admin.full_name is not None:
        existing_admin.full_name = admin.full_name
    if admin.email is not None:
        existing_admin.email = admin.email
    if admin.hashed_password is not None:
        existing_admin.hashed_password = hash_password(admin.hashed_password)

    db.commit()
    db.refresh(existing_admin)
    return existing_admin

def delete_admin(db: Session, admin_id: int):
    admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")

    db.delete(admin)
    db.commit()
    return {"message": "Admin deleted"}