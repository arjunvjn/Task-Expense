from pydantic import BaseModel, Field
from typing import Optional

class UserBase(BaseModel):
    username: str
    
class UserRequest(UserBase):
    password: str
    salary: Optional[float] = Field(0.0, gt=0)