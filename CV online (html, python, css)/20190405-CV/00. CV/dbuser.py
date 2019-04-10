from pymongo import MongoClient

uri = "mongodb+srv://admin:789852@tk-c4e26-ldifb.mongodb.net/test?retryWrites=true"

client = MongoClient(uri)

db = client.test

infuser_collection = db["infuser"]

def infuser(imagebase64,cvtitle,fullname,nominee,dateofbirth,sex,numberphone,addressemail,address,website,awareness,hobby,schoolname,startschool,endschool,majors,describe,companyname,startcompany,endcompany,locationcompany,jobdescription,prize,timeprize,softskill,namecertificate,typecertificate,diffirent,_id_user):
    new_infuser = {
    "image": imagebase64,
    "cvtitle":cvtitle,
    "fullname":fullname,
    "nominee":nominee,
    "dateofbirth":dateofbirth,
    "sex":sex,
    "numberphone":numberphone,
    "addressemail":addressemail,
    "address":address,
    "website":website,
    "awareness":awareness,
    "hobby":hobby,
    "schoolname":schoolname,
    "startschool":startschool,
    "endschool":endschool,
    "majors":majors,
    "describe":describe,
    "companyname":companyname,
    "startcompany":startcompany,
    "endcompany":endcompany,
    "locationcompany":locationcompany,
    "jobdescription":jobdescription,
    "prize":prize,
    "timeprize":timeprize,
    "softskill":softskill,
    "namecertificate":namecertificate,
    "typecertificate":typecertificate,
    "diffirent":diffirent,
    "_id_user":_id_user,
    }
    infuser_collection.insert_one(new_infuser)
    return new_infuser
def search_image(imagebase64):
    image = infuser_collection.find_one({'image': imagebase64})
    return image
def close():
    client.close()
