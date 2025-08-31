from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    hashed_password: str

class UserCreate(UserBase):
    full_name: str

class UserUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    hashed_password: str | None = None

class UserOut(UserCreate):
    id: int

    class Config:
        from_attributes = True