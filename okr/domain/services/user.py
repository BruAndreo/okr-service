from okr.resources.schemas.auth import AuthBody
from okr.resources.schemas.user import UserBody
from okr.domain.models.user import User as UserModel
from okr.utils.jwt import JWT
from okr.domain.repositories.user_repository import UserRepository
from okr.utils.uuid import uuid_generator

class User:

    def create_user(self, user_body: UserBody):
        user = UserModel(**user_body, user_id=uuid_generator())
        user_repo = UserRepository()
        user_repo.insert_user(user)
        return user.user_id

    def authenticate_user(self, auth: AuthBody):
        user_repo = UserRepository()
        user = user_repo.find_by_auth(auth.email, auth.password)

        if not user:
            raise Exception("Not found user")
        return JWT.generate({
            "user_id": user.get('user_id'),
            "username": user.get('name'),
            "email": user.get('email'),
            "birthdate": user.get('birthdate')
        })