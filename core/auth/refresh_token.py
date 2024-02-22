import time
from typing import Dict
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def refresh_token_response(access_token: str):
    return {
        "access_token": access_token
    }


def generate_access_token(user_id: str) -> Dict[str, str]:
    access_token_payload = {
        "user_id": user_id,
        "expires": time.time() + 600  # 10 minutes
    }
    access_token = jwt.encode(access_token_payload,
                              JWT_SECRET, algorithm=JWT_ALGORITHM)
    return refresh_token_response(access_token)
