n = int(input("nhap so n : "))

if n == 0:
        print(1)
else:
        m = 1
        for i in range(1,n+1):
                m *= i
        print(m)
