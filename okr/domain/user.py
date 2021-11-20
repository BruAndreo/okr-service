from okr.resources.schemas.user import UserBody
from okr.domain.models.user import User as UserModel
from okr.data.db import db

import uuid
class User:

    def create_user(self, user_body: UserBody):
        user = UserModel(**user_body, user_id=self._generate_user_id())
        db.users.insert(user.dict())
        return user.user_id

    def _generate_user_id(self) -> str:
        return str(uuid.uuid4())