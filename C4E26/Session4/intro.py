# person = ["H.Duc", 24, "Haiphong", 11, False, 430, True]

# person = {}
# print(person)
# print(type(person))

# key: Value cho biết ý nghĩa của value(nội dung dữ liệu)
# person = {
#     "name": "H.Duc"
# }
# print(person)

person = { #unordered: không qtr thứ tự
    "name": "H.Duc",
    "age": 24,
    "location": "Haiphong",
    "status": False,
    "favs": ["book", "music", "movies"]
}
# bóc dữ liệu chỉ quan tâm tới hiện tại đang ở đâu, nên đặt biến cho các lớp tách tới đâu 
# fs = person["favs"]
# for fav in fs:
#     print(fav)

# print(fs[1])

#truy cập thẳng k thông qua biến gần như mảng 2 chiều
#print(person["favs"][1])

# person["friend_count"] = 450
# print(person)

# person["age"] += 2
# del person["age"]
# print(person)

# in phần tử key của dictionary(mỗi cái xuống dòng 1 lần)
# for k in person.keys():
#     print(k, person[k])

#in phần tử value của dictionary(mỗi cái xuống dòng 1 lần)
# for v in person.values():
#     print(v)

# in cả 2 phần tử theo cặp trong dictionary(mỗi cái xuống dòng 1 lần)
for k,v in person.items():
    print(k,v)

### các loại này thuộc Lookup(tra cứu, tìm kiếm)
#tạo ra một dictionary trong đó chứa DA để tra cứu
#cho người dùng nhập key và in ra kết quả

#in ra toàn bộ dữ liệu trong dictionary
# print(person)
# người dùng nhập
# k = input("nhập ")
# kiểm tra có trong dictionary hay không??
# if k in person:
#     print(person[k])
# else:
#     print("Not")
#truy cập vào từng phần tử trong dictionary
# print(person[k])
