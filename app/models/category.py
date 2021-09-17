from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
# from app.models.expense import Expense


class CategoryBase(SQLModel):
    name: Optional[str]

    expenses: List["Expense"] = Relationship(back_populates="category")


class Category(CategoryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CategoryCreate(CategoryBase):
    name: str


class CategoryUpdate(CategoryBase):
    id: int
    pass
