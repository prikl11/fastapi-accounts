from decimal import Decimal
from fastapi import HTTPException
from schemas import AccountCreate, AccountUpdate
from models import Accounts
from sqlalchemy.orm import Session

def create_account(db: Session, account: AccountCreate):
    new_account = Accounts(user_id=account.user_id, balance=account.balance)
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

def read_account(db: Session, account_id: int):
    account = db.query(Accounts).filter(Accounts.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    return account

def read_accounts(db: Session):
    return db.query(Accounts).all()

def update_account(db: Session, account_id: int, account: AccountUpdate):
    existing_account = db.query(Accounts).filter(Accounts.id == account_id).first()
    if not existing_account:
        raise HTTPException(status_code=404, detail="Account not found")

    if account.user_id is not None:
        existing_account.user_id = account.user_id
    if account.balance is not None:
        existing_account.balance = Decimal(account.balance)

    db.commit()
    db.refresh(existing_account)
    return existing_account

def delete_account(db: Session, account_id: int):
    account = db.query(Accounts).filter(Accounts.id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    db.delete(account)
    db.commit()
    return {"message": "Account deleted"}