from random import randint
x = randint(0, 100)
cloudy = ''' Hello '''
if x < 30:
    print("Rainy")
elif x < 60:
    print(cloudy)
else :
    print("Sunny")