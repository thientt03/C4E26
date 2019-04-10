import turtle
window = turtle.Screen()
window.title("Square")
zo = turtle.Turtle()

def draw_star(x,y,length):
        zo.penup()
        zo.goto(x,y)
        zo.pendown()
        for i in range(5):
                zo.left(144)
                zo.forward(length)

        

draw_star(10,10,100)
window.mainloop()

    
