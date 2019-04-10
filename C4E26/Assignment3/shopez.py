print("Hello")
print("Welcome to our shop,What do you want(C,R,U,D) ")

listitems = ["T-Shirt", "Sweater"]
x = input("Nhập chữ cái:")
loop = True

while loop:
    if x == "R":
        print(listitems[0],",", listitems[1])
        break
    elif x == "C":
        newitem = input("input-item: ")
        listitems.append(newitem)
        print(*listitems, sep = ", ")
        break
    elif x == "U":
        z = int(input("index-change : "))
        y = input("input-item : ")
        listitems[z] = y
        print(listitems)
        break
    elif x == "D":
        delete = int(input("input-delete : "))
        del listitems[delete]
        print(listitems)
        break
    else:
        print("What do you want(C,R,U,D)")
        x = input("Nhập chữ cái:")
   

