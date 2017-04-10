import pymongo
import config

class UsersDb:

    def __init__(self, db):
        self.__db = db
        self.__collection = db.users

    def getUser(self, username):
        return self.__collection.find_one({"_id": username})

    def createUser(self, username, first_name, last_name):
        user = {
            "_id": username,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "admin_on": [],
            "passed": []
        }
        self.__collection.insert_one(user)
        return user

    def getOrCreateUser(self, username, first_name, last_name):
        user = self.getUser(username)
        if user:
            return user
        return self.createUser(username, first_name, last_name)

    def updateUser(self, db_user):
        self.__collection.update_one({"_id": db_user["_id"]}, {"$set": db_user})

    def getTop(self, top_number=10):
        return self.__collection.aggregate([
            {
                "$project": {
                    "passed": 1,
                    "username": 1,
                    "first_name": 1,
                    "last_name": 1,
                    "passed_length": {"$size": "$passed"}
                }
            },
            {"$sort": {"passed_length": -1}}
        ])
