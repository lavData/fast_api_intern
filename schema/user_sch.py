from typing import Optional
from pydantic import BaseModel, Field


class BaseUser(BaseModel):
    username: str
    name: str
    full_name: Optional[str] = None
    address: str


class UserIn(BaseUser):
    password: str


class UserOut(BaseUser):
    ...


class UserInDb(BaseUser):
    password_hashed: str


class UserUpdate(BaseModel):
    password: Optional[str] = None
    name: Optional[str] = None
    full_name: Optional[str] = None
    address: Optional[str] = None




