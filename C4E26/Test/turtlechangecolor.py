import turtle
def draw_s(animal, size): # def kiểu như là một hàm chức năng có chứa tham số truyền vào 
        for i in ["red", "purple", "blue"]:
                animal.forward(size)
                animal.left(90)
                animal.color(i)

window = turtle.Screen()
window.bgcolor("lightblue")
window.title("Hello Turtle")

alex = turtle.Turtle()
alex.pensize(5)
size = 20
for i in range(15):
        draw_s(alex, size)
        size += 10
        alex.forward(10)
        alex.right(18)
window.mainloop()