from pymongo import MongoClient
from okr.config import settings

client = MongoClient(settings.database.host, settings.database.port)
db = client[settings.database.db_name]