import json
from fastapi.encoders import jsonable_encoder
from lunch_order.schema import food_sch
from lunch_order import config
from lunch_order.config import Config

config = Config()


def read_foods():
    return json.load(open(config.FOOD_DB_PATH))


def insert_food(food_in: food_sch.Food):
    foods_db = read_foods()
    foods_db[food_in.food_id] = food_in.dict()

    with open(config.FOOD_DB_PATH, 'w') as f:
        json.dump(foods_db, f, indent=4)


def update_food(food_id: str, food_update: food_sch.FoodUpdate):
    foods_db = read_foods()
    food_db = foods_db[food_id]
    food_model = food_sch.Food(**food_db)
    updated_food = food_update.dict(exclude_unset=True)
    updated_food = food_model.copy(update=updated_food)
    foods_db[food_id] = jsonable_encoder(updated_food)

    with open(config.FOOD_DB_PATH, 'w') as f:
        json.dump(foods_db, f, indent=4)


def delete_food(food_id: str):
    foods_db: dict = read_foods()
    foods_db.pop(food_id)

    with open(config.FOOD_DB_PATH, 'w') as f:
        json.dump(foods_db, f, indent=4)


def price_food(food_id: str):
    return read_foods()[food_id]["price"]
