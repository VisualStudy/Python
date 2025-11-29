import turtle

t = turtle.Turtle()
t.shape("turtle")

def move(f, a):
    t.forward(f)
    t.right(a)

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

move(200, 90)

turtle.done()