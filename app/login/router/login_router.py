from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.login.controller.login_controller import userLogin
from core.config.database import get_db
from app.login.schema.login_schema import UserLogin

signin = APIRouter()


class Signin:
    @signin.post("/login")
    def login(userlogin: UserLogin, session: Session = Depends(get_db)):
        userdata = userLogin(session, userlogin)
        return userdata
