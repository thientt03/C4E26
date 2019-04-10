ani = {
    "move": [2,4,3],
    "sex": ["đực", "cái","lưỡng tính","Cả 3"],
    "places": ["sky", "tree","land"],
}

person = {
    "move": [2,4,3],
    "sex": ["trai", "gái","lưỡng tính"],
    "places": ["sky", "tree","land"],
}
# check = [1,2,3]
print("con chó đi bằng mấy chân: ")
fd = ani["move"]

for i in range(len(fd)):
    print(i+1, fd[i], sep = ", ")

ans = int(input("Nhập số: "))
loop = True
while loop:
    
    if ans == 2:
        print("Pigo")

    else:
        print("False")
        k = input("You can countie .... ?? Y/S ")
        if k == "Y":
            print("Động vật có những giới tính gì??")
            fs = ani["sex"]
            for j in range(len(fs)):
                print(j+1, fs[j], sep = ", ")
            
            n = int(input("nhập số"))
            if n == 4:
                print("Pigo")
            else:
                print("No")
        else:
            print("Over")
        break
    loop = False
    
