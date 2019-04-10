question = {
    "number": [35,36,40,44],
    "number2": [5,6,7,8],
    "number3": [9,10,11,12],
}
count = 0
ques = 0
print("If x = 8, then what is value of 4(3+x) ??")
fs = question["number"]
for i in range(len(fs)):
    print(i+1, fs[i], sep = ", ")
ans = int(input("Your choice: "))
if ans == 4:
    print(":)) Bingo")
    count += 1
    ques +=1
    
    print("Lional Messi wears some clothes ??")
    for j in range(len(question["number3"])):
        print(j+1, question["number3"][j], sep = ", ")
    m = int(input("nhập số: "))
    if m == 2:
        print("Bingo")
        count += 1
    else:
        print("HiHi")
    ques += 1
    print("Over")
    
else: 
    ques +=1
    print(":(( Over")
    print("You can countie...(Y/N) ??")
    k =  input("nhập : ")
    if k == "Y":
        print("Critino Ronaldo wears some clothes ??") 
        for i in range(len(question["number2"])):
            print(i+1,question["number2"][i], sep = ", ")
        
        n = int(input("nhập số : "))   
        if n == 3:
            print(":)) Bingo")
            count += 1
            ques += 1
        else:
            print("Nghỉ")
            ques += 1
        
    else:
        print("End :))")
print(count,"/",ques)


