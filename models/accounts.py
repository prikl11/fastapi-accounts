from database import Base
from sqlalchemy import Column, Integer, ForeignKey, DECIMAL

class Accounts(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), index=True)
    balance = Column(DECIMAL, default=0)