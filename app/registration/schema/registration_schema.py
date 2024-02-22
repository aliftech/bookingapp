from fastapi import Form
from pydantic import BaseModel, EmailStr, root_validator
import bcrypt


class CreateRegistration(BaseModel):
    name: str = Form(...)
    email: EmailStr = Form
    phone: str = Form(...)
    address: str = Form(...)
    password: str = Form(...)

    @root_validator(pre=True)
    def hash_password(cls, values):
        if 'password' in values:
            hashed_password = bcrypt.hashpw(
                values['password'].encode('utf-8'), bcrypt.gensalt())
            values['password'] = hashed_password.decode('utf-8')
        return values
