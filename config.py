
from pydantic import BaseSettings


class Config(BaseSettings):
    USER_DB_PATH: str = "lunch_order/data/user.json"
    FOOD_DB_PATH: str = "lunch_order/data/food.json"
    ORDER_DB_PATH: str = "lunch_order/data/order.json"
