from okr.data.db import db

class MongoBuilder():

    def __init__(self, collection):
        self._conn = db[collection]