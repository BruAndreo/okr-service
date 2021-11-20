from okr.resources.schemas.user import UserBody
from okr.domain.models.user import User as UserModel

import uuid
class User:

    def create_user(self, user_body: UserBody):
        user = UserModel(**user_body, user_id=self._generate_user_id())
        print(user)
        # register in db
        return user.user_id

    def _generate_user_id(self) -> str:
        return str(uuid.uuid4())