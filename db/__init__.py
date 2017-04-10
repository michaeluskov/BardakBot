import config
from pymongo import MongoClient

from db.codes import CodesDb
from db.users import UsersDb

client = MongoClient(config.MONGODB_URL)
db = client[config.MONGODB_DATABASE]

users = UsersDb(db)
codes = CodesDb(db)
