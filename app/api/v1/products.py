from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.get("")
def read_products():
    return {"message": "hola"}
