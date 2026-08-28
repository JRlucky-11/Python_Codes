from turtle import *
t = Turtle()
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
t4 = Turtle()
t5 = Turtle()
# Shape names -> 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
t.shape("arrow")
t.rt(170)
t.fd(202)

t1.shape("turtle")
t1.pencolor("red")
t1.shapesize(10, 20, 5)
t1.rt(160)
t1.fd(202)

t2.shape("circle")
t2.rt(150)
t2.fd(202)

t3.shape("square")
t3.rt(140)
t3.fd(202)

t4.shape("triangle")
t4.rt(130)
t4.fd(202)

t5.shape("classic")
t5.rt(120)
t5.fd(202)

done()