from decimal import Decimal
from pydantic import BaseModel
from uuid import UUID

class WebhookPayload(BaseModel):
    transaction_id: UUID
    user_id: int
    account_id: int
    amount: Decimal
    signature: str