from typing import Optional
from pydantic import BaseModel


class BaseOrder(BaseModel):
    food_ids: dict[str, int]


class UserOrder(BaseOrder):
    ...


class Order(BaseOrder):
    order_id: str
    user_id: str
    quantity: int
    total_price: int
    delivered: bool


class OrderUpdate(BaseModel):
    user_id: Optional[str]
    food_ids: Optional[dict[str, int]]
    quantity: Optional[int]
    total_price: Optional[int]
    delivered: Optional[bool]


