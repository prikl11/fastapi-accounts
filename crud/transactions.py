from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from decimal import Decimal

from models import Accounts, Transaction

def process_transaction(db: Session, transaction_id: str, user_id: int, account_id: int, amount: Decimal):
    try:
        with db.begin():
            existing = db.query(Transaction).filter(Transaction.id == transaction_id).first()
            if existing:
                return False

            acc = db.query(Accounts).filter(Accounts.id == account_id).with_for_update().first()
            if not acc:
                acc = Accounts(id=account_id, user_id=user_id, balance=Decimal(0))
                db.add(acc)
                db.flush()

            tx = Transaction(
                transaction_id=transaction_id,
                user_id=user_id,
                account_id=acc.id,
                amount=Decimal(str(amount))
            )
            db.add(tx)

            acc.balance += Decimal(str(amount))

        return True
    except IntegrityError:
        return False