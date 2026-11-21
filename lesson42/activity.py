import turtle 

turtle.Screen().bgcolor("Yellow")
sc = turtle.Screen()
sc.setup(500, 600)

turtle.title("Welcome to turtle window")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)

turtle.done()