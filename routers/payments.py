from fastapi import APIRouter, HTTPException
from crud import process_transaction
from . import SessionDep
from schemas import WebhookPayload
from security import compute_signature
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

router = APIRouter()

@router.post("/webhook")
def webhook(payload: WebhookPayload, db: SessionDep):
    expected_signature = compute_signature(
        account_id=payload.account_id,
        amount=payload.amount,
        transaction_id=str(payload.transaction_id),
        user_id=payload.user_id,
        secret_key=SECRET_KEY
    )
    if expected_signature != payload.signature:
        raise HTTPException(status_code=401, detail="Invalid signature")

    success = process_transaction(
        db=db,
        transaction_id=str(payload.transaction_id),
        user_id=payload.user_id,
        account_id=payload.account_id,
        amount=payload.amount
    )

    if success:
        return {"status": "ok"}
    else:
        return {"status": "already_processed"}