from turtle import *
t = Turtle()

t.fillcolor("green")
t.begin_fill()

t.penup()
t.goto(50,50)
t.pendown()

t.goto(-50,50)
t.goto(-50,-50)
t.goto(50,-50)
t.goto(50,50)

t.end_fill()

done()