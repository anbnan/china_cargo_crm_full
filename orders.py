from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Order(BaseModel):
    id: int
    client_id: int
    status: str
    total_price: float
    comment: str

orders_db: List[Order] = []

@router.post("/orders/")
def create_order(order: Order):
    orders_db.append(order)
    return order

@router.get("/orders/")
def list_orders():
    return orders_db
