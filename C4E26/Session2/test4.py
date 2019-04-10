import turtle

window = turtle.Screen()
window.title("Hello")

z = turtle.Turtle()
z.shape("turtle")
n =10
for i in range(100):
        z.stamp() # đóng dấu rùa ở điểm quay đầu
        z.forward(n)
        z.left(90)
        n += 10 # cộng thêm 10 ở mỗi lần lặp

window.mainloop()