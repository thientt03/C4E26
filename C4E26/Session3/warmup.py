

while True:
    yob_str = input("năm sinh : ")
    if yob_str.isdigit():
        yob = int(yob_str)
        if 1960 < yob < 2020:
            
            break            
        else:
            print("nhập lại")
    else:
        print("you must provide a number")

age = 2019 - yob
print(age)



