from lunch_order.core.respons_ex.pattern import pattern_ex

EX_FOOD_DB = {
    "food1": {
        "food_id": "food1",
        "type": "thuc an",
        "name": "bun cha",
        "price": 20000,
        "description": "thom ngon tuyet voi"
    },
    "food2": {
        "food_id": "food2",
        "type": "thuc uong",
        "name": "sua tuoi chan trau duong den",
        "price": 40000,
        "description": "ngon, nhung hai gan hai than"
    },
    "food3": {
        "food_id": "food3",
        "type": "thuc an",
        "name": "com chien xoi mo",
        "price": 22000,
        "description": "ga don rum, nhieu mo, an kho tieu"
    }
}


GET_ALL_200 = pattern_ex("Return successful", EX_FOOD_DB)


GET_ALL_204 = pattern_ex(
    "Return successful",
    {
        "detail": "Database no content"
    }
)


GET_ONE_200 = pattern_ex("Return successful", EX_FOOD_DB["food1"])


ID_NOT_FOUND_404 = pattern_ex(
    "Return fail",
    {
        "detail": "Food item not found"
    }
)


POST_FOOD_200 = pattern_ex("Create successful", EX_FOOD_DB["food1"])


EXISTS_FOOD_409 = pattern_ex(
    "Create fail",
    {
        "detail": "Food item existed"
    }
)


PATCH_FOOD_200 = pattern_ex("Update successful", EX_FOOD_DB["food1"])


DELETE_FOOD_200 = pattern_ex(
    "Delete successful",
    {
        "detail": "Delete food successful"
    },
)
