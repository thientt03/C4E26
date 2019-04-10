import turtle
window = turtle.Screen()
window.title("Square")
zo = turtle.Turtle()

def draw_square(cd , colr):
    for i in range(4):
        zo.color(colr)
        zo.forward(cd)
        zo.left(90)
        

draw_square(100,"red")
window.mainloop()

    
