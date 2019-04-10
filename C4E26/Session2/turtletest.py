import turtle 
window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("hello, Turtle")

zero = turtle.Turtle()
zero.shape("turtle")


zero.color("blue")
zero.pensize(7)

zero.forward(100)
zero.left(90)

test = turtle.Turtle()
test.shape("turtle")
test.pensize(3)
for i in ["blue", "yellow", "red"]:
    test.stamp()
    test.color(i)
    test.forward(100)
    test.left(90)

window.mainloop()