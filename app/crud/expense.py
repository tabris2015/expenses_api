from typing import Optional, List
from sqlmodel import Session
from app.crud.base import CRUDBase
from app.models.expense import Expense, ExpenseCreate, ExpenseUpdate


class ExpenseCRUD(CRUDBase[Expense, ExpenseCreate, ExpenseUpdate]):
    pass


expense = ExpenseCRUD(Expense)
