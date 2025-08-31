from . import SessionDep
from crud import create_account, read_account, update_account, delete_account, read_accounts, transfer
from fastapi import APIRouter
from schemas import AccountOut, AccountCreate, AccountUpdate

router = APIRouter()

@router.post("/register/account", response_model=AccountOut)
def create_account_route(db: SessionDep, account: AccountCreate):
    return create_account(db, account)

@router.get("/accounts", response_model=list[AccountOut])
def read_accounts_route(db: SessionDep):
    return read_accounts(db)

@router.get("/accounts/{account_id}", response_model=AccountOut)
def read_account_route(db: SessionDep, account_id: int):
    return read_account(db, account_id)

@router.patch("/accounts/{account_id}", response_model=AccountOut)
def update_account_route(db: SessionDep, account_id: int, account: AccountUpdate):
    return update_account(db, account_id, account)

@router.delete("/accounts/{account_id}", response_model=AccountOut)
def delete_account_route(db: SessionDep, account_id: int):
    return delete_account(db, account_id)

@router.patch("/accounts/{account_id}", response_model=AccountOut)
def transfer_route(db: SessionDep, account_id: int, amount: int, sign: str):
    return transfer(db, account_id, amount, sign)