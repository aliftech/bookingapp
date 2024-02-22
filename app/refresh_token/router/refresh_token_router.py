from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.config.database import get_db
from app.refresh_token.controller.refresh_token_controller import get_access_token
from app.refresh_token.schema.refresh_token_schema import UserToken

token = APIRouter()


class RefreshToken:
    @token.post("/token")
    def generate_token(usertoken: UserToken, session: Session = Depends(get_db)):
        userdata = get_access_token(session, usertoken)
        return userdata
