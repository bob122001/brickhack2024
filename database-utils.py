from  pymongo import MongoClient
mongo_client = MongoClient("localhost")
db = mongo_client["lawyercraft"]
users = db['users']

def add_user():
    pass