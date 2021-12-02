from okr.config import settings
from okr.data.builder import MongoBuilder
from okr.domain.models.user import User

class UserRepository(MongoBuilder):

    _collection = settings.database.user_collection

    def __init__(self):
        super().__init__(self._collection)

    def insert_user(self, user: User):
        return self._conn.insert_one(user.dict())

    def find_by_auth(self, email, password):
        return self._conn.find_one({ "email": email, "password": password })