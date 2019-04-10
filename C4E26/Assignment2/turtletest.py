import turtle
window = turtle.Screen()
window.bgcolor("lightblue")
window.title("Hello Turtle")

pi = turtle.Turtle()
pi.color("red")
pi.shape("turtle")

for i in range(4):
    pi.right(30)
    pi.forward(100)
    pi.left(60)
    pi.forward(100)
    pi.left(120)
    pi.forward(100)
    pi.left(60)
    pi.forward(100)
    pi.right(120)

window.mainloop()