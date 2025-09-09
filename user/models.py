from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    salary = Column(Float, default=0)

    expenses = relationship('Expense', back_populates='user', cascade="all, delete-orphan")
