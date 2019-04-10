inventory = {
    "gold": 500,
    "pouch": ["flint", "twine", "gemstore"],
    "backpack": ["xylophone","dagger", "bedroll", "bread loaf"]
}
# cập nhật một cặp key-value:
inventory["pocket"] = ["seasell", "strange berry", "lint"]
print(inventory)

# xóa một phần tử trong key:
inventory["backpack"].remove("dagger")
print(inventory)

# thêm số vào key:
x = int(inventory["gold"] + 50)
inventory["gold"] = x
print(inventory)
