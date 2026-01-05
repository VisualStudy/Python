import turtle

t = turtle.Turtle()

n = int(input('3~5 사이의 정수: '))
d = int(input('10~30 사이의 큰 정수: '))

def pg(n, d):
    for i in range(n):
        t.forward(d)
        t.right(360 / n)

for i in range(6):
    pg(n, d)
    t.right(360 / 6)

print(f"rabarata{n}")
    
turtle.done()