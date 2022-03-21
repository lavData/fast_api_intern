from typing import Optional
from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Path,
)
from lunch_order.schema import food_sch
from lunch_order.core.db import food_db
from lunch_order.core.respons_ex import food_ex

router = APIRouter(
    prefix="/foods",
    tags=["foods"]
)


@router.get(
    "/",
    response_model=dict[str, food_sch.Food],
    summary="Read all foods",
    responses={
        status.HTTP_200_OK: food_ex.GET_ALL_200,
        status.HTTP_204_NO_CONTENT: food_ex.GET_ALL_204
    }
)
async def read_foods():
    """
    Get all foods with all information:
    - **food_id**: id food item
    - **type**: type of food, ex (nuoc, thuc an)
    - **name**: name of food
    - **price**: price of food
    - **description**: description of food
    """
    foods_db: dict = food_db.read_foods()
    if len(foods_db.keys()) == 0:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Database no content.")
    else:
        return foods_db


@router.get(
    "/{food_id}/",
    response_model=food_sch.Food,
    summary="Read food item",
    responses={
        status.HTTP_200_OK: food_ex.GET_ONE_200,
        status.HTTP_404_NOT_FOUND: food_ex.ID_NOT_FOUND_404
    }
)
async def read_food(
        food_id: Optional[str] = Path(
            ...,
            title="Query food item",
            description="Query information of one food item"
        )
):
    if food_id not in food_db.read_foods():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Food item not found!")
    else:
        return food_db.read_foods()[food_id]


@router.post(
    "/",
    response_model=food_sch.Food,
    summary="Create a food item",
    responses={
        status.HTTP_200_OK: food_ex.POST_FOOD_200,
        status.HTTP_409_CONFLICT: food_ex.EXISTS_FOOD_409
    }
)
async def create_food(food_in: food_sch.Food):
    if food_in.food_id in food_db.read_foods():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Food item existed!")
    else:
        food_db.insert_food(food_in)
        return food_in


@router.patch(
    "/{food_id}/",
    response_model=food_sch.FoodUpdate,
    summary="Update food item",
    responses={
        status.HTTP_200_OK: food_ex.PATCH_FOOD_200,
        status.HTTP_404_NOT_FOUND: food_ex.ID_NOT_FOUND_404
    }
)
async def update_food(
        *,
        food_id: Optional[str] = Path(
            ...,
            title="Update food item",
            description="Update information of one food item"
        ),
        food_update: food_sch.FoodUpdate):
    if food_id not in food_db.read_foods():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Food item not found!")
    else:
        food_db.update_food(food_id, food_update)
        return food_db.read_foods()[food_id]


@router.delete(
    "/{food_id}",
    response_model=dict[str, str],
    responses={
        status.HTTP_200_OK: food_ex.DELETE_FOOD_200,
        status.HTTP_404_NOT_FOUND: food_ex.ID_NOT_FOUND_404
    }
)
async def delete_food(
        food_id: Optional[str] = Path(
            ...,
            title="Delete food item",
            description="Delete food item"
        )):
    if food_id not in food_db.read_foods():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Food item not found!")
    else:
        food_db.delete_food(food_id)
        return {"detail": "Delete food success!"}
