import random
import string

import config

class CodesDb:

    def __init__(self, db):
        self.__db = db
        self.__collection = db.codes

    def generateCode(self, room_name):
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        code_from_db = self.__collection.find_one({"_id": code})
        if code_from_db is not None:
            return self.generateCode(room_name)
        self.__collection.insert_one({
            "_id": code,
            "code": code,
            "room_name": room_name
        })
        return code
