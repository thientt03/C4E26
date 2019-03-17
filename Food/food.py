from db import food_collection
from bson import ObjectId
def add_food(name, price):
    new_food = {
        "name": name,
        "price": price,
    }
    food_collection.insert_one(new_food)

def get(query):
    food_list = food_collection.find(query)
    return food_list

def get_by_id(id):
    f = food_collection.find_one({"_id": ObjectId(id)})
    return f
def delete_by_id():
    food_collection.delete_one({"_id": ObjectId(id)})
def update_by_id(id, name, price):
    query = {"_id": ObjectId(id)}
    updater = { 
        "$set": {"price":price}, 
        "$set": {"name": name},
    } # $inc, $dec, $set, $unset
    food_collection.find_one_and_update(query, updater)

if __name__ == '__main__':
    print(*get({}), sep="\n")
    # food_collection.delete_one({
    #     "_id": ObjectId("5c81241b40d18611ecb741d8")
    # })
    # while True:
    #     n = input("nhập: ")
    #     m = int(input("nhập: "))
        
    #     add(n, m)
    
    # food_list = food_collection.find(
    #     {
    #         "price": { "$lte": 300000, "$gte": 20000}
    #     }# query
    # ) #lazy loading
    # f = get_by_id("5c81241b40d18611ecb741d8")
    # if f != None: #found
    #     print(f["name"])
    # else:
    #     print("No")
    