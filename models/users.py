from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Column, Integer, String, Text

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    full_name = Column(String(50), index=True)
    hashed_password = Column(Text)

    accounts = relationship("Account", back_populates="user")
    # transactions = relationship("Transaction", back_populates="user")