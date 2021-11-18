from pydantic import BaseModel, Field, validator
from bson import ObjectId
import datetime

class PyObjectId(ObjectId):
    """ Custom Type for reading MongoDB IDs """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object_id")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class User(BaseModel):
    user_id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    email: str
    password: str
    birthdate: datetime.date
    created_at: datetime.datetime = datetime.datetime.now()

    @validator("birthdate", pre=True)
    def parse_birthdate(cls, value):
        return datetime.datetime.strptime(
            value,
            "%d/$m/%Y"
        ).date()
