from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Column, Integer, Text, ForeignKey, DECIMAL

class Payments(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(Text, index=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    amount = Column(DECIMAL, index=True)

    user = relationship("User", back_populates="transactions")
    # account = relationship("Account", back_populates="transactions")
