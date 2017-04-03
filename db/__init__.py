import config
from pymongo import MongoClient
from .users import UsersDb

client = MongoClient(config.MONGODB_URL)
db = client[config.MONGODB_DATABASE]

users = UsersDb(db)
