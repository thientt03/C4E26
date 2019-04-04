from db import user_collection
def find_by_username(username):
    f = user_collection.find_one({"username": username})
    return f
def find_by_password(password):
    p = user_collection.find_one({"password": password})
    return p