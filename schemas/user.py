from pydantic import BaseModel
from fastapi.security import HTTPBasicCredentials


class UserSignIn(HTTPBasicCredentials):
    class Config:
        json_schema_extra = {
            "example": {"username": "abdul.youngest.dev", "password": "3xt3m#"}
        }


class UserData(BaseModel):
    firstname: str
    lastname: str
    username: str

    class Config:
        json_schema_extra = {
            "example": {
                "firstname": "Abdulazeez",
                "lastname": "Adeshina",
                "username": "abdul.youngest.dev",
            }
        }
