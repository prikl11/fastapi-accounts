from fastapi import FastAPI
from database import Base, engine
from routers import users, admins, accounts

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router, tags=["users"])
app.include_router(admins.router, tags=["admins"])
app.include_router(accounts.router, tags=["accounts"])