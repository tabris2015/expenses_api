from typing import Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class ProductBase(SQLModel):

    name: Optional[str]
    price: Optional[float]


class Product(ProductBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class ProductCreate(ProductBase):
    name: str
    price: float


class ProductUpdate(ProductBase):
    id: int
    pass


class ProductResponse(Product):
    class Config:
        orm_mode = True
