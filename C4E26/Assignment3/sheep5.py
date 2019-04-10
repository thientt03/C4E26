print("Hello, My name is thien and these are my ship size")
sheeplist = [5, 7, 300, 90, 24, 50, 75] 
x = input("Nhập số tháng : ")
loop = True
while loop:
    sheeplist = [50 + x for x in sheeplist]
    sheeplist.sort()
    sheeplist.reverse()
    
    if sheeplist[0] == 350:
        sheeplist[0] = 8
        sheeplist.sort()
        loop = False
        print(sheeplist)

    