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

    async def authenticate_user(self, auth: AuthBody):
        user = await db.users.find_one({ "email": auth.email, "password": auth.password })
        print(type(user))
        if not user:
            raise Exception("Not found user")
        return jwt.encode({
            "user_id": user.user_id,
            "username": user.name,
            "email": user.email,
            "birthdate": user.birthdate
        }, "secret", algorithm="HS256")