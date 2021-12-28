from typing import Dict
from okr.data.db import db

class MongoBuilder():

    def __init__(self, collection):
        self._conn = db[collection]

    def insert_one(self, document_body: Dict):
        return self._conn.insert_one(document_body)