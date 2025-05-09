from fastapi import APIRouter
from ..database import get_db
from fastapi.params import Depends
from sqlalchemy.orm import session
from ..models import Transaction
from datetime import date
from typing import Optional



router = APIRouter(tags=['Analytics'])

@router.get('/summary/')

def transaction_summary(start_date : Optional[date] = None, end_date : Optional[date] = None,   db:session = Depends(get_db)):
    query = db.query(Transaction)
    if start_date:
        query = query.filter(Transaction.date >= start_date)
    if end_date:
        query = query.filter(Transaction.date <= end_date)
    transactions = query.all()
    total_income  = sum (t.amount for t in transactions if t.transaction_type == 'income')
    total_expense = sum (t.amount for t in transactions if t.transaction_type == 'expense')
    balance = total_income - total_expense

    return {'total_income':total_income,
            'total_expense':total_expense,
            'balance':balance}
    