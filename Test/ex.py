from db import tt_collection
def add(img):
    new_od = {
        "img": img,
    }
    tt_collection.insert_one(new_od)