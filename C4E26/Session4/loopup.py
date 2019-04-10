teen_code = {
    "pt": "Phát triển",
    "eny": "Em người yêu",
    "any": "Anh người yêu",
    "stt": "Status",
}
loop = True
while loop:
    k = input("enter Your Words ")
    if k in teen_code:
        print(teen_code[k])
    else:
        print("Not")
        n = input("Có muốn đóng góp k ?? (YES or NO)").upper()
        if n == "YES":
            l = input("nhập value: ")
            teen_code[k] = l
            print(teen_code) 
        else:
            print("bạn muốn tiếp tục k ??")
    if k == "exit":
        loop = False    
            

            
            
    