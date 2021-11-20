from pydantic import BaseModel
from typing import Any
import uuid
import datetime
import uuid

class User(BaseModel):
    user_id: str
    name: str
    email: str
    password: str
    birthdate: datetime.datetime
    created_at: datetime.datetime = datetime.datetime.now()
