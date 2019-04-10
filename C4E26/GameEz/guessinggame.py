import random
x = random.randint(0,100)
n = int(input("số:"))
count = 0
loop = True
while loop:
        if x > n:
                print("số nhỏ hơn")
                n = int(input("số:"))
                count += 1
        elif x < n:
                print("số lớn hơn")
                n = int(input("số:"))
                count += 1
        elif x == n:
                count += 1
                print("pigo")
                loop = False

print(count)
        