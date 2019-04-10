items = ["x", "y", "z", "t"]
# for i, vard in enumerate(items, 1):
#     print(i, vard.upper(), sep = ", ")

lama = ["I", "II", "III","IV"]
# for i in range(len(items)):
#     for x in range():
#         print(lama[x], items[i])
# for i, f in enumerate(items, 1):
#     print(lama[i], f, sep = ", ")

# zip có nhiệm vụ nhóm các phần tử có chung chỉ số thành 1 nhóm
print(*zip(lama, items))
for p, f in zip(lama, items):    
    print(p, f)