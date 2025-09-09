from pydantic import BaseModel, Field
from typing import Optional

class ExpenseRequest(BaseModel):
    name: str
    amount: float = Field(..., gt=0)
    category: str
    user_id: int