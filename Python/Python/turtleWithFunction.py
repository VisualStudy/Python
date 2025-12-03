import turtle

t = turtle.Turtle()

def pg(n, d):
    for i in range(n):
        t.forward(d)
        t.right(360 / n)

def tmoving(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

turtle.done()