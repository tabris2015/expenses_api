from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from app.models.category import Category


class ExpenseBase(SQLModel):
    description: Optional[str]
    amount: Optional[int]
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    category: Optional[Category] = Relationship(back_populates="expenses")


class Expense(ExpenseBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class ExpenseCreate(ExpenseBase):
    description: str
    amount: int


class ExpenseUpdate(ExpenseBase):
    id: int
    pass
