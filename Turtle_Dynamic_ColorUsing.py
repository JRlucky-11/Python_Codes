from turtle import *
colors = ['green', 'blue', 'red']
t1 = Turtle()

t1.speed(0)

for i in range(36):
    t1.pencolor(colors[i % 3]) # using dynamic color
    t1.circle(100)
    t1.left(10)

done()