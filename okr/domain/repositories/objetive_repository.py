from okr.data.builder import MongoBuilder

class ObjectiveRepository(MongoBuilder):

    _collection = "objetives"

    def __init__(self):
        super().__init__(self._collection)