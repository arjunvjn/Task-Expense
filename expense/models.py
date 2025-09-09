from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
import datetime
import enum
from sqlalchemy.orm import relationship

from database import Base

class Category(enum.Enum):
    Food = 'Food'
    Transport = 'Transport'
    Entertainment = 'Entertainment'
    Utilities = 'Utilities'
    Other = 'Other'

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(Enum(Category), default=Category.Other)
    created_at = Column(DateTime, default=datetime.datetime.now)

    user = relationship('User', back_populates='expenses')