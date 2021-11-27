from pydantic import BaseModel, validator
import okr.utils.crypt as crypt

class AuthBody(BaseModel):
    email: str
    password: str

    @validator("password")
    def crypt_password(cls, value):
        return crypt.encrypt(value)
