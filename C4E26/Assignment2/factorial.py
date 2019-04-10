n = int(input("nhập số : "))
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(n))