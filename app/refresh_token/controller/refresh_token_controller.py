from sqlalchemy.orm import Session
from datetime import datetime
from app.refresh_token.schema.refresh_token_schema import UserToken
from app.login.model.refresh_token_model import RefreshToken
from core.helper.response_helper import ResponseData
from core.auth.refresh_token import generate_access_token


def get_access_token(session: Session, usertoken: UserToken) -> ResponseData:
    current_time = datetime.now()
    check_token = session.query(RefreshToken).filter(
        RefreshToken.token == usertoken.refresh_token and RefreshToken.expired_at < current_time).first()

    if check_token is not None:
        user_id = check_token.user_id
        token = generate_access_token(user_id)
        response = ResponseData(
            status_code=200,
            message='Access token generated successfully.',
            data=token
        )
        return response

    response = ResponseData(
        status_code=400,
        message='Invalid or expired refresh token.',
    )
    return response
