from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi_jwt_auth import AuthJWT

from database import get_db
from .schemas import UserRequest
from .models import User

router = APIRouter(
    prefix='/users',
    tags=['User']
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(body: UserRequest, db: Session=Depends(get_db)):
    try:
        if db.query(User).filter(User.username == body.username).first():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Username already exist')
        hashed_password = pwd_context.hash(body.password)
        user = User(username=body.username,password=hashed_password, salary=body.salary)
        db.add(user)
        db.commit()
        return 'User Created'
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
