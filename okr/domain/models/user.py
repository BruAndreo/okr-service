from pydantic import BaseModel
import datetime

class User(BaseModel):
    user_id: str
    name: str
    email: str
    password: str
    birthdate: datetime.datetime
    created_at: datetime.datetime = datetime.datetime.now()
