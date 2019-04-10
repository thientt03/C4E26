items = ["death note", "netflix", "teaching"]
for i, f in enumerate(items):
    print(i +1, f, sep = ", ")
x = input("delete: ")
# items.pop(x-1)
# print(items)

loop = True
while loop:
    if x.isdigit():
        items.pop(int(x)-1)
        print(items)
    elif x.isalpha():
        items.remove(x)
        print(items)
    else:
        print("again ??")
        x = input("delete: ")
    loop = False
