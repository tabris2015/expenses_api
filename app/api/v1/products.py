from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session, select
from app.models.product import Product, ProductResponse, ProductCreate, ProductUpdate
from app.database.session import get_session

router = APIRouter()


@router.get("", response_model=List[ProductResponse])
def read_products(db: Session = Depends(get_session)):
    products = db.exec(select(Product)).all()
    return products


@router.post("", response_model=ProductResponse)
def create_product(*, db: Session = Depends(get_session), product: ProductCreate):
    db_product = Product.from_orm(product)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
