import time
from typing import Dict
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


def token_response(access_token: str, refresh_token: str):
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


def signJWT(user_id: str) -> Dict[str, str]:
    access_token_payload = {
        "user_id": user_id,
        "expires": time.time() + 600  # 10 minutes
    }
    access_token = jwt.encode(access_token_payload,
                              JWT_SECRET, algorithm=JWT_ALGORITHM)

    refresh_token_payload = {
        "user_id": user_id,
        "expires": time.time() + 604800  # 7 days
    }
    refresh_token = jwt.encode(
        refresh_token_payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(access_token, refresh_token)


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {"Expired token. "}
