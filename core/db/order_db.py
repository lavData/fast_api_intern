import json
from fastapi.encoders import jsonable_encoder
from lunch_order.schema import order_sch
from lunch_order import config
from lunch_order.config import Config

config = Config()


def read_order():
    return json.load(open(config.ORDER_DB_PATH))


def insert_order(order_in: order_sch.Order):
    orders_db = read_order()
    orders_db[order_in.order_id] = order_in.dict()

    with open(config.ORDER_DB_PATH, 'w') as f:
        json.dump(orders_db, f, indent=4)


def update_order(order_id: str, order_update: order_sch.OrderUpdate):
    orders_db = read_order()
    order_db = orders_db[order_id]
    order_model = order_sch.Order(**order_db)
    updated_order = order_update.dict(exclude_unset=True)
    updated_order = order_model.copy(update=updated_order)
    orders_db[order_id] = jsonable_encoder(updated_order)

    with open(config.ORDER_DB_PATH, 'w') as f:
        json.dump(orders_db, f, indent=4)


def delete_order(order_id: str):
    orders_db: dict = read_order()
    orders_db.pop(order_id)

    with open(config.ORDER_DB_PATH, 'w') as f:
        json.dump(orders_db, f, indent=4)


def create_order_id():
    order_id = read_order().keys()
    order_id = [int(k[5:])for k in order_id]      # Remove prefix order
    return "order" + str(max(order_id) + 1)


def order_user(user_id: str):
    return {k: v for k, v in read_order().items() if v["user_id"] == user_id}
