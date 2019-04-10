
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
# in ra fruit, prices, stock
while True:
    for k in prices:
        k = input("nhập tên sản phẩm : ")
        print(k)
        print("prices :",prices[k])
        print("stock :",stock[k])

# in ra fruit, prices, stock và total
total = 0
for l in prices:
    print(l)
    print("prices :",prices[l])
    print("stock :",stock[l])
    total += prices[l]*stock[l]
print()
print(total)