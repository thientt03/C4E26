from pymongo import MongoClient

uri = "mongodb+srv://admin:789852@tk-c4e26-ldifb.mongodb.net/test?retryWrites=true"

#1 connect
client = MongoClient(uri)

#2 get DB
db = client.test

#3 get Collection
food_collection = db["food"]

# #4 Creat a new document
# new_food = {
#     "name": "cơm rang",
#     "price": 300000,
# }#document

#5 insert new document into collection
# food_collection.insert_one()

#6 close connection
def close():
    client.close()


