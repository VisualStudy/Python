import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color

d = 50
r = 90

for i in range(4):
    t.forward(50)
    t.right(90)


# t.forward(50)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(50)  ;세미콜론 x
# t.right(90)

fruit = ['apple', 'banana', "kiwi", "pear"]
print(fruit[0])
print(fruit[-1])
print(fruit[3])

fruit[3] = "strawberry"
print(fruit[3])


turtle.done
