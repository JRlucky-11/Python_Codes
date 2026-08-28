from turtle import *
t = Turtle()

t.penup()
t.goto(200,200)
t.pendown()

t.fillcolor("green")
t.begin_fill()

t.goto(-200,200)
t.goto(-200,-200)
t.goto(200,-200)
t.goto(200,200)

t.end_fill()

t.ht()

done()