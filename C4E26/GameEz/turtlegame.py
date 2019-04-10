import turtle

window = turtle.Screen()
window.title("Hello Turtle")
window.bgcolor("white")

po = turtle.Turtle()
po.shape("turtle")
colors = ["red", "blue", "brown", "yellow", "grey"]

loop = True
n = 3
while loop:
    for i in range(n):
        po.color(colors[i])
        po.forward(100)
        po.left(120)
        n += 1
        
        
    # for i in range(4):
    #     po.color(colors[i])
    #     po.forward(100)
    #     po.left(90)
    
    # for i in colors:
    #     po.color(i)
    #     po.forward(100)
    #     po.left(60)

    # for i in colors:
    #     po.color(i)
    #     po.forward(100)
    #     po.left(72)

    
    
    # for i in colors:
    #     po.color(i)
    #     po.forward(100)
    #     po.left(180-((7-2)*180/7))
    
    
    loop = False
window.mainloop()