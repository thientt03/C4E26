from random import randint,choice
from calc import evaluate
# import calc

x = randint(0,10)
y = randint(0,10)
pt = choice(["+", "-", "*", "/"])
err = randint(-1,1)
r = evaluate(x,y,pt) +err

# string formating
s = f"{x} {pt} {y} = {r}"
print(s)

# user_answer = input("Y/N")
