from fastapi import FastAPI

from database import Base, engine
from user.routes import router as user_router
from expense.routes import router as expense_router

Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(user_router)
app.include_router(expense_router)
