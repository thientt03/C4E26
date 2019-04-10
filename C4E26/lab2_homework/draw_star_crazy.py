import turtle
window = turtle.Screen()
window.title("Square")
zo = turtle.Turtle()
zo.speed(0)
zo.color('blue')

def draw_star(x, y, length):
        zo.penup()
        zo.goto(x,y)
        zo.pendown()
        for i in range(5):
                zo.left(144)
                zo.forward(length)

for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)

window.mainloop()

