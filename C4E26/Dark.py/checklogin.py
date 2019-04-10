# username = input("Nhập username : ")
# password = input("Nhập password : ")

loop = True
while loop:
    username = input("Nhập username : ")
    password = input("Nhập password : ")
    if not (username.isalnum() and password.isalnum()):
        print("Sai username hoặc password")
                
    else:        
        if username == "admin" and password == "admin":
            print("Đăng nhập thành công ^^")
            print("Hello!!")
        elif username == "salesman" and password == "salesman":
            print("Đăng nhập thành công ^^")
            print("Say hi !!")            
        else:
            print("Who are you??")
        
    loop = False


