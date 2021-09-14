from typing import Any, List, Type, TypeVar
from sqlmodel import Session, select
from app.crud.base import CRUDBase, ModelType
from app.models.category import Category, CategoryCreate, CategoryUpdate
from app.models.expense import Expense

ExpenseModelType = TypeVar("ExpenseModelType", bound=Expense)


class CategoryCRUD(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    def __init__(self, model: Type[ModelType], expense_model: Type[ExpenseModelType]):
        super().__init__(model)
        self.expense_model = expense_model

    def get_expenses(
            self,
            db: Session,
            category_id: Any,
            *,
            skip: int = 0,
            limit: int = 100) -> List[ExpenseModelType]:
        statement = select(self.expense_model).where(self.expense_model.category_id == category_id).offset(skip).limit(limit)
        expenses = db.exec(statement).all()
        return expenses


category = CategoryCRUD(Category, Expense)
