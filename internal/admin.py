from fastapi import APIRouter, HTTPException
# from ..dependencies import get_token_header,get_query_token

router = APIRouter()
#
# router = APIRouter(
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header())],
#     responses={404: {"description": "Not found"}}
# )
#
# fake_admin_db = {"admin01": {"name": "lav"}, "admin02": {"name": "leanhvu"}}
#
#
# @router.get("/")
# async def read_admin():
#     return fake_admin_db
#
#
# @router.get("/{admin_id}", summary="Read admin")
# async def read_admin(admin_id: str):
#     if admin_id not in fake_admin_db:
#         raise HTTPException(status_code=404, detail="Admin not found")
#     return {"name": fake_admin_db[admin_id]["name"], "admin_id": admin_id}
#
#
# @router.put(
#     "/{admin_id}",
#     tags=["custom"],
#     responses={403: {"description": "Operation forbidden"}}
# )
