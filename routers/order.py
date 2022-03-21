from typing import Optional
from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Path,
)
from lunch_order.schema import order_sch
from lunch_order.core.db import order_db
from lunch_order.core.respons_ex import order_ex

router = APIRouter(
    prefix="/order",
    tags=["order_items"]
)


@router.get(
    "/",
    response_model=dict[str, order_sch.Order],
    summary="Read all order items",
    responses={
        status.HTTP_200_OK: order_ex.GET_ALL_200,
        status.HTTP_204_NO_CONTENT: order_ex.GET_ALL_204
    }
)
async def read_order_items():
    """
    Get all order items with all information:
    - **order_id**: id order item
    - **user_id**: user id owner of this order item
    - **food_ids**: dictionary of food id and quantity that user order
    - **quantity**: total quantity of food
    - **total_price**: total price that user has to pay
    - **delivered**: state of delivered
    """
    order_items_db: dict = order_db.read_order()
    if len(order_items_db.keys()) == 0:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="Database no content.")
    else:
        return order_items_db


@router.get(
    "/{order_id}/",
    response_model=order_sch.Order,
    summary="Read order item",
    responses={
        status.HTTP_200_OK: order_ex.GET_ONE_200,
        status.HTTP_404_NOT_FOUND: order_ex.ID_NOT_FOUND_404
    }
)
async def read_food(
        order_id: Optional[str] = Path(
            ...,
            title="Read order item",
            description="Read information of one order item"
        )
):
    if order_id not in order_db.read_order():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order item not found!")
    else:
        return order_db.read_order()[order_id]


@router.post(
    "/",
    response_model=order_sch.Order,
    summary="Create a order item",
    responses={
        status.HTTP_200_OK: order_ex.POST_ORDER_200,
        status.HTTP_409_CONFLICT: order_ex.EXISTS_ORDER_409
    }
)
async def create_food(order_in: order_sch.Order):
    if order_in.order_id in order_db.read_order():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Order item existed!")
    else:
        order_db.insert_order(order_in)
        return order_in


@router.patch(
    "/{order_id}/",
    response_model=order_sch.Order,
    summary="Update order item",
    responses={
        status.HTTP_200_OK: order_ex.PATCH_ORDER_200,
        status.HTTP_404_NOT_FOUND: order_ex.ID_NOT_FOUND_404
    }
)
async def update_order(
        *,
        order_id: Optional[str] = Path(
            ...,
            title="Update order item",
            description="Update information of one order item"
        ),
        order_updated: order_sch.OrderUpdate):
    if order_id not in order_db.read_order():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order item not found!")
    else:
        order_db.update_order(order_id, order_updated)
        return order_db.read_order()[order_id]


@router.delete(
    "/{order_id}",
    response_model=dict[str, str],
    responses={
        status.HTTP_200_OK: order_ex.DELETE_ORDER_200,
        status.HTTP_404_NOT_FOUND: order_ex.ID_NOT_FOUND_404
    }
)
async def delete_order(
        order_id: Optional[str] = Path(
            ...,
            title="Delete order item",
            description="Delete order item"
        )):
    if order_id not in order_db.read_order():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order item not found!")
    else:
        order_db.delete_order(order_id)
        return {"Message": "Delete success!"}
