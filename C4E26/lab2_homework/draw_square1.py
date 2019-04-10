import turtle
window = turtle.Screen()
window.title("Square")
zo = turtle.Turtle()

def draw_square(cd, colr):
    for i in range(4):
        zo.color(colr)
        zo.forward(cd)
        zo.left(90)

for i in range(30):
    draw_square(i * 5, 'red')
    zo.left(17)
    zo.penup()
    zo.forward(i * 2)
    zo.pendown()
    
window.mainloop()
