from pydantic import EmailStr, BaseModel, root_validator
import bcrypt
from typing import Annotated
from fastapi import Body


class UserLogin(BaseModel):
    email: Annotated[EmailStr, Body(...)]
    password: Annotated[str, Body(...)]

    @root_validator(pre=True)
    def hash_password(cls, values):
        if 'password' in values:
            hashed_password = bcrypt.hashpw(
                values['password'].encode('utf-8'), bcrypt.gensalt())
            values['password'] = hashed_password.decode('utf-8')
        return values

    class Config:
        schema_extra = {
            "example": {
                "email": "abdulazeez@x.com",
                "password": "weakpassword"
            }
        }
