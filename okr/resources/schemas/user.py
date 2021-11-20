from pydantic import BaseModel, validator
import okr.utils.crypt as crypt
import datetime

class UserBody(BaseModel):
    name: str
    email: str
    password: str
    birthdate: datetime.datetime

    @validator("password")
    def crypt_password(cls, value):
        return crypt.encrypt(value)
