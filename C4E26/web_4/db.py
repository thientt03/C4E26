from pymongo import MongoClient

uri = "mongodb+srv://admin:789852@tk-c4e26-ldifb.mongodb.net/test?retryWrites=true"
# connert db
client = MongoClient(uri)

#get db
db = client.test

#get collection
car_collection = db["car"]

if __name__ == '__main__':
# creat db
    new_car = [
        {
            "producer": "Suzuki",
            "price": 1,
            "color": "black",
        },
        {
            "producer": "Mercedes",
            "price": 5,
            "color": "white",
        },
        {
            "producer": "Ferarri",
            "price": 10,
            "color": "black",
        },
        {
            "producer": "Lamborghini",
            "price": 12,
            "color": "yellow",
        },
        {
            "producer": "chilini",
            "price": 9,
            "color": "gray",
        },
    ]
    #insert new document in collection
    car_collection.insert_many(new_car)

    #close connert
def cloose():
    client.close()