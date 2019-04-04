from pymongo import MongoClient

uri = "mongodb+srv://admin:789852@tk-c4e26-ldifb.mongodb.net/test?retryWrites=true"

client = MongoClient(uri)

db = client.test

test_collection = db["test_img"]





def close():
    client.close()

