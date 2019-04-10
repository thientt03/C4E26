import turtle
window = turtle.Screen()
window.bgcolor("lightblue")
window.title("Hello Turtle")

pi = turtle.Turtle()
pi.shape("turtle")

for i in range(6):
    pi.color("pink")
    pi.forward(100)
    pi.left(60)

for i in range(4):
    pi.color("red")
    pi.forward(100)
    pi.left(90)

for i in range(5):
    pi.color("blue")
    pi.forward(100)
    pi.left(72)

for i in range(3):
    pi.color("blue")
    pi.forward(100)
    pi.left(120)
        
        

window.mainloop()
