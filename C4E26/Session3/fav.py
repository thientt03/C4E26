items = ["death note", "netflix", "teaching"]
for i, f in enumerate(items):
    print(i +1, f, sep = ", ")

# a = "*"
# for i in range(30):
#     print(a, end = "")

print()
x = int(input("Possition you want to update : "))
y = input("Your replacing favorite ? ")

# Kiểm tra xem có phải kí tự đặc biệt hay nhập sai hay không nếu nhập sai thì in ra thông báo lỗi??
# loop = True
# while loop:
#     if not y.isalnum():
#         print("Again??")
#         break
#     else:
#         y = input("Your replacing favorite ? ")
#     loop = False

items[x-1] = y

print(items)