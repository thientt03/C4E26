from random import randint
count = 0
que = 0
while True:
    x = randint(0,10)
    y = randint(0,10)
    err = randint(-1,1)
    print( x,"+",y,"=",x+y+err)
    user = input("nhập Y/N ")
    if (x+y == x+y+err) and (user == "Y"):
        print("Yad")
        que += 1
        count += 1
    elif (x+y == x+y+err) and (user == "N"):
        print("no!!")
        que += 1
    elif (x+y != x+y+err) and (user == "N"):
        print("Yad")
        que += 1
        count += 1
    elif (x+y != x+y+err) and (user == "Y"):
        print("no!!")
        que += 1
    elif (user == "exit"):
        print(count,"/",que)
        break
        