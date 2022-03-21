import json
from fastapi.encoders import jsonable_encoder
from lunch_order.schema import user_sch, order_sch
from lunch_order.core.db import food_db, order_db
from lunch_order import config
from lunch_order.config import Config

config = Config()


def read_user():
    return json.load(open(config.USER_DB_PATH))


def insert_user(user_in: user_sch.UserIn):
    users_db = read_user()
    users_db[user_in.username] = user_in.dict()

    with open(config.USER_DB_PATH, 'w') as f:
        json.dump(users_db, f, indent=4)


def update_user(user_id: str, user_update: user_sch.UserUpdate):
    users_db = read_user()
    user_db = users_db[user_id]
    user_model = user_sch.UserIn(**user_db)
    updated_user = user_update.dict(exclude_unset=True)
    updated_user = user_model.copy(update=updated_user)
    users_db[user_id] = jsonable_encoder(updated_user)

    with open(config.USER_DB_PATH, 'w') as f:
        json.dump(users_db, f, indent=4)


def delete_user(user_id: str):
    users_db: dict = read_user()
    users_db.pop(user_id)

    with open(config.USER_DB_PATH, 'w') as f:
        json.dump(users_db, f, indent=4)


def order_food(user_id: str, user_order: order_sch.UserOrder):
    order = user_order.dict()

    order["order_id"] = order_db.create_order_id()      # Insert order_id to order
    order["user_id"] = user_id      # Insert user id to order

    foods: dict = order["food_ids"]
    quantity = sum([v for k, v in foods.items()])
    order["quantity"] = quantity        # quantity

    for k in foods.keys():
        foods[k] = foods[k] * food_db.price_food(k)
    total_price = sum([v for k, v in foods.items()])
    order["total_price"] = total_price      # total_price

    order["delivered"] = "true"

    order = order_sch.Order(**order)        # Convert to model
    order_db.insert_order(order)
    return order


def user_order(user_id: str):
    return order_db.order_user(user_id)
