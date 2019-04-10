from pymongo import MongoClient

uri = "mongodb+srv://admin:789852@tk-c4e26-ldifb.mongodb.net/test?retryWrites=true"

client = MongoClient(uri)

db = client.test

user_collection = db["user"]

if __name__ == '__main__':
    new_user = {
        "username": "noname1",
        "password": "c4e26",
        }
    user_collection.insert_one(new_user)

def close():
    client.close()

