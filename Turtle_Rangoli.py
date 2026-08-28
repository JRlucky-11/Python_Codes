from turtle import *
t1 = Turtle()
t2 = Turtle()

# t1.speed(0)
# t2.speed(0)
t1.color("red", "green")
t2.color("blue", "yellow")
t1.begin_fill()
t2.begin_fill()

for i in range(6):
    t1.circle(100)
    t1.right(144)
   
t1.end_fill()
t2.end_fill()

done()
