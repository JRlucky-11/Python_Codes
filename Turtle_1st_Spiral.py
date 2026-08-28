from turtle import *
t1 = Turtle()

t1.speed(9)
t1.pencolor("blue")

for i in range(100):
    t1.forward(i * 4)
    t1.left(60)

done()