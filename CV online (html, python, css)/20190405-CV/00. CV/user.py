from db import user_collection
from bson import ObjectId
from dbuser import infuser_collection
def find_by_username(username):
    f = user_collection.find_one({"username": username})
    return f
def find_by_password(password):
    p = user_collection.find_one({"password": password})
    return p
def get_by_id(id):
    f=user_collection.find_one({"_id":ObjectId(id)})
    return f
def get_cv(username):
    a=infuser_collection.find_one({"_id_user":username})
    return a
