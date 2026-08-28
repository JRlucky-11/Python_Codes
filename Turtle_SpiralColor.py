from turtle import *
colors = ['green', 'blue', 'red']
t1 = Turtle()

t1.speed(0)

for i in range(150):
    t1.pencolor(colors[i % 3]) # using dynamic color
    t1.forward(i)
    t1.left(59)

done()