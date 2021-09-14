from typing import Optional
from sqlmodel import SQLModel, Field


class CategoryBase(SQLModel):
    name: Optional[str]


class Category(CategoryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CategoryCreate(CategoryBase):
    name: str


class CategoryUpdate(CategoryBase):
    id: int
    pass
