from pydantic import BaseModel
from decimal import Decimal

class AccountCreate(BaseModel):
    user_id: int
    balance: Decimal

class AccountUpdate(BaseModel):
    user_id: int | None = None
    balance: Decimal | None = None

class AccountOut(AccountCreate):
    id: int

    class Config:
        from_attributes = True