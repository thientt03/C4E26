from ex1connert import db
post_collection = db["posts"]
new_post = {
    "title": "Zero- where start",
    "author": "Trần Khánh Thiện C4E26",
    "content": "Some pain will make you change",
}
post_collection.insert_one(new_post)