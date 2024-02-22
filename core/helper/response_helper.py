from fastapi import HTTPException
from typing import Any, Dict


class ResponseData:
    def __init__(self, status_code: int, message: str, data: Any = None):
        self.status_code = status_code
        self.message = message
        self.data = data

    def as_dict(self) -> Dict[str, Any]:
        response_dict = {
            'status_code': self.status_code,
            'message': self.message,
            'data': self.data,
        }
        return response_dict


def create_api_exception(response: ResponseData) -> HTTPException:
    return HTTPException(status_code=response.status_code, detail=response.as_dict())
