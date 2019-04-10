from random import *
from calc import evaluate
def generate_quiz():
    x = randint(0,10)
    y = randint(0,10)
    err = randint(-1,1)
    op = choice(["+","-","*","/"]) 
    re = 0
    
    if op == "+":
        re = x+y
    elif op == "-":
        re = x-y
    elif op == "*":
        re = x*y
    elif op == "/":
        if y != 0:
            re = x / y
        else:
            re = 0
       
    result = re + err
    
    return [x, y, op, result]
    
def check_answer(x, y, op, result, user_choice):
    if (evaluate(x, y, op) == result) and (user_choice == True ):
        return True 
    elif (evaluate(x, y, op) == result) and (user_choice == False):
        return False
        
    elif (evaluate(x, y, op) != result) and (user_choice == False):
        return True
        
    elif (evaluate(x, y, op) != result) and (user_choice == True):
        return False
    # elif (user_choice == "exit"):
    #     print(count,"/",que)
   
