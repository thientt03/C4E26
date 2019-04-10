import turtle

window = turtle.Screen()
window.title("Hello Turtle")
window.bgcolor("white")

po = turtle.Turtle()
po.shape("turtle")
colors = ["red", "blue", "brown", "yellow", "grey"]

loop = True
while loop:
    po.color(colors[0])
    for i in colors:
        po.forward(100)
        po.left(120)
        
        
    for i in colors:
        
        po.forward(100)
        po.left(90)
    
    for i in colors:
        po.color(i)
        po.forward(100)
        po.left(60)

    for i in colors:
        po.color(i)
        po.forward(100)
        po.left(72)

    
    
    for i in colors:
        po.color(i)
        po.forward(100)
        po.left(180-((7-2)*180/7))
    
    
    loop = False
window.mainloop()