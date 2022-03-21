from typing import Optional
from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Path,
)
from lunch_order.schema import user_sch, order_sch
from lunch_order.core.db import user_db, food_db
from lunch_order.core.respons_ex import user_ex

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.get(
    "/",
    response_model=dict[str, user_sch.UserOut],
    summary="Read all users",
    responses={
        status.HTTP_200_OK: user_ex.GET_ALL_200,
        status.HTTP_204_NO_CONTENT: user_ex.GET_ALL_204
    }
)
async def read_users():
    """
    Get all users with all information without password:
    - **username**: each user must have a unique username
    - **name**: required, name of user
    - **fullname**: Optional, fullname of user.
    - **address**: required, where the user live
    """
    users_db: dict = user_db.read_user()
    if len(users_db.keys()) == 0:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Database no content")
    return users_db


@router.get(
    "/{user_id}/",
    response_model=user_sch.UserOut,
    responses={
        status.HTTP_200_OK: user_ex.GET_ONE_200,
        status.HTTP_404_NOT_FOUND: user_ex.ID_NOT_FOUND_404
    }
)
async def read_user(
        user_id: str = Path(
            ...,
            title="Query user",
            description="Query information of one user"
        )
):
    if user_id not in user_db.read_user():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User item not found!")
    else:
        return user_db.read_user()[user_id]


@router.post(
    "/",
    response_model=user_sch.UserOut,
    responses={
        status.HTTP_200_OK: user_ex.POST_USER_200,
        status.HTTP_409_CONFLICT: user_ex.EXISTS_USER_409
    }
)
async def create_user(user_in: user_sch.UserIn):
    if user_in.username in user_db.read_user():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User item existed!")
    else:
        user_db.insert_user(user_in)
        return user_in


@router.patch(
    "/{user_id}/",
    response_model=user_sch.UserOut,
    responses={
        status.HTTP_200_OK: user_ex.PATCH_USER_200,
        status.HTTP_404_NOT_FOUND: user_ex.ID_NOT_FOUND_404
    }
)
async def update_user(
        *,
        user_id: Optional[str] = Path(
            ...,
            title="Update user",
            description="Update information of one user"
        ),
        user_update: user_sch.UserUpdate):
    if user_id not in user_db.read_user():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")
    else:
        user_db.update_user(user_id, user_update)
        return user_db.read_user()[user_id]


@router.delete(
    "/{user_id}/",
    response_model=dict[str, str],
    responses={
        status.HTTP_200_OK: user_ex.DELETE_USER_200,
        status.HTTP_404_NOT_FOUND: user_ex.ID_NOT_FOUND_404
    }
)
async def delete_user(
        user_id: Optional[str] = Path(
            ...,
            title="Delete user",
            description="Delete user"
        )
):
    if user_id not in user_db.read_user():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User item not found!")
    else:
        user_db.delete_user(user_id)
        return {"detail": "Delete user success!"}


@router.post(
    "/{user_id}/",
    tags=["order_items"],
    summary="Order food for user",
    response_model=order_sch.Order,
    responses={
        status.HTTP_200_OK: user_ex.ORDER_FOOD_200,
        status.HTTP_409_CONFLICT: user_ex.ORDER_FOOD_409,
        status.HTTP_404_NOT_FOUND: user_ex.ORDER_FOOD_404
    }
)
async def order_food(
        *,
        user_id: Optional[str] = Path(
            ...,
            title="Order food",
            description="Order food"
        ),
        user_order: order_sch.UserOrder
):
    if user_id not in user_db.read_user():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User item not found!")

    food_ids_in = user_order.dict()["food_ids"].keys()
    food_ids_db = food_db.read_foods().keys()
    if not all(item in food_ids_db for item in food_ids_in):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="")

    return user_db.order_food(user_id, user_order)


@router.get(
    "/{user_id}",
    tags=["order_items"],
    summary="Read history order of user",
    response_model=dict[str, order_sch.Order],
    responses={
        status.HTTP_200_OK: user_ex.GET_ORDER_200,
        status.HTTP_204_NO_CONTENT: user_ex.GET_ORDER_204,
        status.HTTP_404_NOT_FOUND: user_ex.ID_NOT_FOUND_404
    }
)
async def read_order(user_id: str):
    if user_id not in user_db.read_user():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User item not found!")

    user_order = user_db.user_order(user_id)
    if user_order == {}:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Order history empty")
    return user_order
