from turtle import *
t = Turtle()
t1 = Turtle()
t2 = Turtle()

# Increase Pensize...
t.pensize(2)
t1.pensize(2)
t2.pensize(2)

t1.hideturtle()
t2.hideturtle()
t.hideturtle()

# Using Dynamic Color -> Geometrical Spiral
colors1 = ["green", "red", "blue", "Orange"]

# Speed Control
t.speed(9)
t1.speed(9)
t2.speed(9)

# Moving 't'
t.penup()
t.bk(350)
t.pendown()

# Moving "t1"
t1.penup()
t1.lt(60)
t1.bk(150)
t1.pendown()

# Moving "t2"
t2.penup()
t2.lt(120)
t2.bk(150)
t2.rt(120)
t2.fd(60)
t2.pendown()

# Draw a Line
t.pencolor("Red")
t.fd(70)

# Some Space
t.penup()
t.fd(30)
t.pendown()

# Draw a Rectangle
t.pencolor("Blue")
for r in range(2):
    t.fd(90)
    t.lt(90)
    t.fd(45)
    t.lt(90)

# Some Space
t.penup()
t.fd(130)
t.pendown()

# Draw a Square
t.pencolor("Green")
for s in range(4):
    t.fd(90)
    t.lt(90)

# Some Space
t.penup()
t.fd(130)
t.pendown()

# Draw a Triangle
t.pencolor("Orange")
for tr in range(3):
    t.fd(90)
    t.lt(120)

# Some Space
t.penup()
t.fd(170)
t.pendown()

# Draw a Circle
t.pencolor("Brown")
t.circle(40)

# Some Space
t.penup()
t.fd(90)
t.pendown()

# Draw a Hexagon
t.pencolor("red")
for h in range(6):
    t.fd(40)
    t.lt(60)

# Draw a Geometrical Spiral Web
for sp in range(50):
    t1.pencolor(colors1[sp % 4])
    t1.fd(sp * 2)
    t1.lt(60)

# Draw a Star
t2.pencolor("blue")
for st in range(5):
    t2.fd(100)
    t2.rt(144)

done()