from pydantic import BaseModel
from decimal import Decimal

class PaymentCreate(BaseModel):
    transaction_id: str
    account_id: int
    user_id: int
    amount: Decimal

class PaymentOut(PaymentCreate):
    id: int

    class Config:
        from_attributes = True