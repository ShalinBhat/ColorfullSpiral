import turtle

colors = ['red', 'yellow', 'green', 'purple', 'blue', 'brown', 'orange']

t= turtle.Pen()
t.speed(10)

turtle.bgcolor("black")

for x in range(200):
    t.pencolor(colors[x%7])
    t.width(x/200 + 1)
    t.forward(x)
    t.left(59)

turtle.done()
t.speed(50)