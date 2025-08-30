from pydantic import BaseModel, EmailStr

class AdminBase(BaseModel):
    email: EmailStr
    password: str

class AdminCreate(AdminBase):
    full_name: str

class AdminUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    password: str | None = None

class AdminOut(AdminCreate):
    id: int

    class Config:
        from_attributes = True