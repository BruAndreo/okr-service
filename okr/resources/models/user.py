from pydantic import BaseModel, validator
from bson import ObjectId
import datetime
import uuid
import okr.utils.crypt as crypt

class User(BaseModel):
    user_id: str = str(uuid.uuid4())
    name: str
    email: str
    password: str
    birthdate: datetime.datetime
    created_at: datetime.datetime = datetime.datetime.now()

    @validator("password")
    def crypt_password(cls, value):
        return crypt.encrypt(value)
