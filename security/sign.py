import hashlib
from decimal import Decimal


def compute_signature(account_id: int, amount: Decimal, transaction_id: int, user_id: int, secret_key: str) -> str:
    s = f"{account_id}{amount}{transaction_id}{user_id}{secret_key}"
    return hashlib.sha256(s.encode("utf-8")).hexdigest()