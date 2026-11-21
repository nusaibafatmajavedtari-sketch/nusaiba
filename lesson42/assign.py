import turtle

turtle.Screen().bgcolor("black")

turtle.title("Welcome to turtle window")

t= turtle.Turtle()

t.speed("fastest")
t.hideturtle()

def draw_petal(size, color):
    t.color(color)
    t.begin_fill()

    for _ in range(2):
      t.circle( 60)
      t.left(120)
    t.end_fill()

colors= ['red', 'orange', 'yellow', 'green', 'blue', 'violet']

for i in range(36):
    draw_petal(90, colors[i%len(colors)])
    t.right(10)
t.penup()
t.goto(0, -25)
t.pendown()

t.color("white")
t.begin_fill()
t.cirlce(25)
t.end_fill

turtle.done()