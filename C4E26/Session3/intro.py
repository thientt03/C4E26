listitem = ["Com", "Pho", "Bun", "Mien"]

# xóa theo vị trí 
listitem.pop(1)
print(listitem)

# xóa theo nội dụng
listitem.remove("Pho")
print(listitem)

# #for i: dài nhưng có sẵn chỉ số ?
for i in range(len(listitem)):
    print(listitem[i])  

#foreach : thêm biến chỉ số nếu cần ?
x = 1
for i, food in listitem:
    print(x, food, sep = ", ")
    x += 1

#for ... in enumerate(list, n): 
#n là giá trị bắt đầu chạy 
#có khả năng dùng cả chỉ số + giá trị ?
for i, food in enumerate(listitem):
    print(i + 1, food)