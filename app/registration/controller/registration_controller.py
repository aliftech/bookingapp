from datetime import datetime
from app.registration.model.registration_model import Registration
from core.helper.response_helper import ResponseData


def create(session, data) -> ResponseData:
    user_detail = session.query(Registration).filter(
        Registration.email == data.email & Registration.phone == data.phone).first()
    if user_detail is not None:
        response = ResponseData(
            status_code=400, message="Email or phone number must unique.", data=None)
        return response

    current_time = datetime.now()
    user = Registration(name=data.name, email=data.email, phone=data.phone,
                        password=data.password, address=data.address, created_at=current_time)
    session.add(user)
    session.commit()
    session.refresh(user)

    response = ResponseData(
        status_code=200, message="Registration success.", data=None)
    return response
