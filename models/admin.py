from database import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String(50), index=True)
    hashed_password = Column(Text, index=True)