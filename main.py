from fastapi import Depends, FastAPI
from .internal import admin
from lunch_order.routers import foods, users, order


app = FastAPI()
app.include_router(users.router)
app.include_router(foods.router)
app.include_router(order.router)


@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello"}

