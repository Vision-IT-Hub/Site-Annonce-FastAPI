from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr, constr


class RoleEnum(str, Enum):
    user = "User"
    admin = "Admin"
    superUser = "superUsr"


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    photo: str
    role: RoleEnum = RoleEnum.user
    created_at: datetime = None
    updated_at: datetime = None

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    verified: bool = False


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
