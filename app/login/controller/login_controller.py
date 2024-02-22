from datetime import datetime, timedelta
from app.registration.model.registration_model import Registration
from app.login.model.refresh_token_model import RefreshToken
from core.helper.response_helper import ResponseData
from core.auth.token import signJWT


def userLogin(session, data) -> ResponseData:
    user_detail = session.query(Registration).filter(
        Registration.email == data.email and Registration.password == data.password).first()

    if user_detail is not None:
        token = signJWT(user_detail.user_id)
        refresh_token = session.query(RefreshToken).filter(
            RefreshToken.user_id == user_detail.user_id).first()

        current_time = datetime.now()
        if refresh_token is not None:
            refresh_token.token = token["refresh_token"]
            refresh_token.expired_at = current_time + timedelta(days=7)
        else:
            refresh_token = RefreshToken(
                user_id=user_detail.user_id, token=token["refresh_token"], expired_at=current_time + timedelta(days=7), created_at=current_time)
            session.add(refresh_token)

        session.commit()
        session.refresh(refresh_token)

        response = ResponseData(
            status_code=200, message='Login success', data={"token": token})
        return response

    response = ResponseData(
        status_code=404, message='Your email or password is incorrect')
    return response
