from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey, DECIMAL, DateTime, func, UniqueConstraint

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(UUID(as_uuid=True), unique=True, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    amount = Column(DECIMAL, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)

    user = relationship("Users", back_populates="transactions")
    account = relationship("Accounts", back_populates="transactions")

    __table_args__ = (
        UniqueConstraint("transaction_id", name="uq_transaction_id"),
    )
