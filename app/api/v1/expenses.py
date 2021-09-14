from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session, select
from app.models.expense import Expense, ExpenseCreate, ExpenseUpdate
from app.database.session import get_session
from app import crud, schemas


router = APIRouter()


@router.get("", response_model=List[Expense])
def read_expenses(db: Session = Depends(get_session), skip: int = 0, limit: int = 100):
    expenses = crud.expense.get_multi(db, skip=skip, limit=limit)
    return expenses


@router.get("/{id}", response_model=Expense)
def read_expense(*, db: Session = Depends(get_session), id: int):
    expense = crud.expense.get(db, model_id=id)
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense does not exist")
    return expense


@router.post("", response_model=Expense)
def create_expense(*, db: Session = Depends(get_session), expense_in: ExpenseCreate):
    category = crud.category.get(db, expense_in.category_id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category does not exist")

    expense = crud.expense.create(db, obj_in=expense_in)
    return expense


@router.put("", response_model=Expense)
def update_expense(*, db: Session = Depends(get_session), expense_in: ExpenseUpdate):
    expense = crud.expense.get(db, model_id=expense_in.id)
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense does not exist")
    category = crud.category.get(db, expense_in.category_id)
    if expense_in.category_id and not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category does not exist")

    expense = crud.expense.update(db, db_obj=expense, obj_in=expense_in)
    return expense


@router.delete("", response_model=schemas.Message)
def delete_expense(*, db: Session = Depends(get_session), id: int):
    expense = crud.expense.get(db, model_id=id)
    if not expense:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Expense does not exist")
    crud.expense.remove(db, model_id=expense.id)
    return {"message": f"Expense with ID={id} deleted."}
