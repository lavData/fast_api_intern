from lunch_order.core.respons_ex.pattern import pattern_ex
from lunch_order.core.respons_ex import order_ex

EX_USER_DB = {
    "lav": {
        "username": "lav",
        "name": "vu",
        "full_name": None,
        "address": "VN"
    },
    "thin": {
        "username": "thin",
        "name": "thin",
        "full_name": "nguyen van thin",
        "address": "vn",
    },
    "tan": {
        "username": "tan",
        "name": "tan",
        "full_name": "nguyen van tan",
        "address": "vn",
    }
}


GET_ALL_200 = pattern_ex("Return successful", EX_USER_DB)


GET_ALL_204 = pattern_ex(
    "Return successful",
    {
        "detail": "Database no content"
    }
)


GET_ONE_200 = pattern_ex("Return successful", EX_USER_DB["thin"])


ID_NOT_FOUND_404 = pattern_ex(
    "Return fail",
    {
        "detail": "User item not found"
    }
)


POST_USER_200 = pattern_ex("Create successful", EX_USER_DB["thin"])


EXISTS_USER_409 = pattern_ex(
    "Create fail",
    {
        "detail": "User item existed"
    }
)


PATCH_USER_200 = pattern_ex("Update successful", EX_USER_DB["thin"])


DELETE_USER_200 = pattern_ex(
    "Delete successful",
    {
        "detail": "Delete user successful"
    },
)


ORDER_FOOD_200 = pattern_ex("Order successful", order_ex.EX_ORDER_DB["order3"])


ORDER_FOOD_409 = pattern_ex(
    "Order fail",
    {
        "detail": "Have one or more item food not existed"
    }
)

ORDER_FOOD_404 = pattern_ex(
    "Order fail",
    {
        "detail": "User item not found"
    }
)


GET_ORDER_200 = pattern_ex(
    "Return successful",
    {
        "order4": order_ex.EX_ORDER_DB["order4"],
        "order6": order_ex.EX_ORDER_DB["order6"]
    }
)


GET_ORDER_204 = pattern_ex(
    "Return successful",
    {
        "detail": "Order history empty"
    }
)
