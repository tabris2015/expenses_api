from fastapi import APIRouter
from app.api.v1 import products, expenses, categories

api_router = APIRouter()
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(expenses.router, prefix="/expenses", tags=["expenses"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
