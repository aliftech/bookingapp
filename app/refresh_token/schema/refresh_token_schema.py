from pydantic import BaseModel


class UserToken(BaseModel):
    refresh_token: str

    class Config:
        schema_extra = {
            "example": {
                "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo4LCJleHBpcmVzIjoxNjg4ODc5ODgxLjg0MTg2Mzl9.vxcVfc65n48H8OyualymaKTsgfsCi-Ywb6Oyo3Ae_Z8",
            }
        }
