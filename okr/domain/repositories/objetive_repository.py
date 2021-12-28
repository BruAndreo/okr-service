from okr.data.builder import MongoBuilder
from okr.config import settings

class ObjectiveRepository(MongoBuilder):

    _collection = settings.database.objective_collection

    def __init__(self):
        super().__init__(self._collection)