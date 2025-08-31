from pydantic import BaseModel, EmailStr

class AdminBase(BaseModel):
    user_id: int
    email: EmailStr
    hashed_password: str

class AdminCreate(AdminBase):
    full_name: str

class AdminUpdate(BaseModel):
    user_id: int | None = None
    full_name: str | None = None
    email: EmailStr | None = None
    hashed_password: str | None = None

class AdminOut(AdminCreate):
    id: int

    class Config:
        from_attributes = True