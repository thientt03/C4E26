from db import car_collection
from bson import ObjectId
def add(producer, price, color):
    new_car = {
        "producer": producer,
        "price": price,
        "color": color,
    }
    car_collection.insert_many(new_car)

def get(query):
    car_list = car_collection.find(query)
    return car_list

def get_by_id(id):
    f = car_collection.find_one({"_id":ObjectId(id)})
    return f

def delete_by_id(id):
    car_collection.delete_one({"_id": ObjectId(id)})

def update_by_id(id, producer, price):
    query = {"_id": ObjectId(id)}
    updater = {
        "$set": {"producer": producer},
        "$set": {"price": price},
    }
    # $inc, $dec, $set, $unset
    car_collection.find_one_and_update(query, updater)
if __name__ == '__main__':
    print(*get({}), sep="\n")