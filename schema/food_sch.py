from typing import Optional
from pydantic import BaseModel


class Food(BaseModel):
    food_id: str
    type: str
    name: str
    price: int
    description: Optional[str] = None


class FoodUpdate(BaseModel):
    food_id: Optional[str]
    type: Optional[str]
    name: Optional[str]
    price: Optional[int]
    description: Optional[str] = None
