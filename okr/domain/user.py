from fastapi.encoders import jsonable_encoder
from okr.resources.schemas.auth import AuthBody
from okr.resources.schemas.user import UserBody
from okr.domain.models.user import User as UserModel
from okr.data.db import db

import uuid
import jwt

class User:

    def create_user(self, user_body: UserBody):
        user = UserModel(**user_body, user_id=self._generate_user_id())
        db.users.insert(user.dict())
        return user.user_id

    def _generate_user_id(self) -> str:
        return str(uuid.uuid4())

    def authenticate_user(self, auth: AuthBody):
        user = db["users"].find_one({ "email": auth.email, "password": auth.password })
        usr = UserModel(**user)
        if not user:
            raise Exception("Not found user")
        return jwt.encode(jsonable_encoder({
            "user_id": usr.user_id,
            "username": usr.name,
            "email": usr.email,
            "birthdate": usr.birthdate
        }), "secret", algorithm="HS256")