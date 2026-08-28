from turtle import *
t = Turtle()
t1 = Turtle()

# Moving Turtle
t1.penup()
t1.bk(150)
t1.pendown()

# Show "t" Turtle 
for i in range(5):
    t.fd(100)
    t.rt(144)

# Hide "t1" Turtle 
t1.ht() # "ht" -> hideturtle()
t1.pencolor("Red")
for i in range(5):
    t1.fd(100)
    t1.rt(144)

t1.penup()
t1.bk(50)
t1.pendown()

t1.st()
t1.pencolor("Blue")
t1.circle(30)

done()