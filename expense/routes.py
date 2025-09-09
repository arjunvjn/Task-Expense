from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session, selectinload

from database import get_db
from .schemas import ExpenseRequest
from .models import Expense
from user.models import User

router = APIRouter(
    prefix='/expenses',
    tag=['Expense']
)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_post(body: ExpenseRequest, db: Session=Depends(get_db)):
    try:
        expense = Expense(**body.model_dump())
        db.add(expense)
        db.commit()
        return 'Expense Created'
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.get('/{id}')
def get_user_expenses(id: int, db: Session=Depends(get_db)):
    try:
        return db.query(Expense).filter(Expense.user_id == id).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.get('/totals/{id}')
def get_user_expenses(id: int, db: Session=Depends(get_db)):
    try:
        return db.query(User).filter(User.id==id).options(selectinload(User.expenses)).all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
