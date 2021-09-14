from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from app.database.session import get_session
from app import crud, schemas
from app.models.category import Category, CategoryCreate, CategoryUpdate
from app.models.expense import Expense


router = APIRouter()


@router.get("", response_model=List[Category])
def read_categories(db: Session = Depends(get_session), skip: int = 0, limit: int = 100):
    categories = crud.category.get_multi(db, skip=skip, limit=limit)
    return categories


@router.get("/{id}/expenses", response_model=List[Expense])
def read_expenses(db: Session = Depends(get_session), *, id: int, skip: int = 0, limit: int = 100):
    category = crud.category.get(db, model_id=id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category does not exist")

    expenses = crud.category.get_expenses(db, id, skip=skip, limit=limit)
    return expenses


@router.get("/{id}", response_model=Category)
def read_category(*, db: Session = Depends(get_session), id: int):
    category = crud.category.get(db, model_id=id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category does not exist")
    return category


@router.post("", response_model=Category)
def create_category(*, db: Session = Depends(get_session), category_in: CategoryCreate):
    category = crud.category.create(db, obj_in=category_in)
    return category


@router.put("", response_model=Category)
def update_category(*, db: Session = Depends(get_session), category_in: CategoryUpdate):
    category = crud.category.get(db, model_id=category_in.id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category does not exist")
    category = crud.category.update(db, db_obj=category, obj_in=category_in)
    return category


@router.delete("", response_model=schemas.Message)
def delete_category(*, db: Session = Depends(get_session), id: int):
    category = crud.category.get(db, model_id=id)
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category does not exist")
    crud.category.remove(db, model_id=category.id)
    return {"message": f"Category with ID={id} deleted."}
