from pymongo import MongoClient

uri = "mongodb+srv://admin:789852@tk-c4e26-ldifb.mongodb.net/test?retryWrites=true"

client = MongoClient(uri)

db = client.test

test_collection = db["test_img"]

def upload(imagebase64):
    image = {
        'image': imagebase64
    }
    test_collection.insert_one(image)

def search_image(imagebase64):
    image = test_collection.find_one({'image': imagebase64})
    return image

def close():
    client.close()

