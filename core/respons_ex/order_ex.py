from lunch_order.core.respons_ex.pattern import pattern_ex

EX_ORDER_DB = {
    "order1": {
        "order_id": "oder1",
        "user_id": "user1",
        "food_ids": {
            "food1": 2,
            "food2": 1
        },
        "quantity": 3,
        "total_price": 80000,
        "delivered": True
    },
    "order2": {
        "order_id": "order2",
        "user_id": "user2",
        "food_ids": {
            "food1": 1,
            "food2": 2
        },
        "quantity": 3,
        "total_price": 100000,
        "delivered": True
    },
    "order3": {
        "order_id": "order3",
        "user_id": "user3",
        "food_ids": {
            "food2": 2
        },
        "quantity": 3,
        "total_price": 80000,
        "delivered": True
    },
    "order4": {
        "food_ids": {
            "food1": 40000,
            "food2": 40000
        },
        "order_id": "order4",
        "user_id": "lav",
        "quantity": 3,
        "total_price": 80000,
        "delivered": True
    },
    "order5": {
        "food_ids": {
            "food1": 40000,
            "food2": 40000,
            "food3": 66000
        },
        "order_id": "order5",
        "user_id": "thin",
        "quantity": 6,
        "total_price": 146000,
        "delivered": True
    },
    "order6": {
        "food_ids": {
            "food1": 60000
        },
        "order_id": "order6",
        "user_id": "lav",
        "quantity": 3,
        "total_price": 60000,
        "delivered": True
    }
}


GET_ALL_200 = pattern_ex("Return successful", EX_ORDER_DB)


GET_ALL_204 = pattern_ex(
    "Return successful",
    {
        "detail": "Database no content"
    }
)


GET_ONE_200 = pattern_ex("Return successful", EX_ORDER_DB["order2"])


ID_NOT_FOUND_404 = pattern_ex(
    "Return fail",
    {
        "detail": "Order item not found"
    }
)


POST_ORDER_200 = pattern_ex("Create successful", EX_ORDER_DB["order2"])


EXISTS_ORDER_409 = pattern_ex(
    "Create fail",
    {
        "detail": "Order item existed"
    }
)


PATCH_ORDER_200 = pattern_ex("Update successful", EX_ORDER_DB["order2"])


DELETE_ORDER_200 = pattern_ex(
    "Delete successful",
    {
        "detail": "Delete order successful"
    },
)
