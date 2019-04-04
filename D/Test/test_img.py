from bson import *
from db import *
with open(index1.jpg, mode='rb') as f:
      image = {
          "title": 'image',
          "name": 'check it',
          "screen_shot": Binary(f.read())
      }
test_collection.insert_one(image)