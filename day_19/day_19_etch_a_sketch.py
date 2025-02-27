from turtle import Turtle, Screen

# Etch-A-Sketch
turtle = Turtle()


def forward():
    turtle.forward(10)

def backward():
    turtle.backward(10)

def right():
    turtle.right(10)

def left():
    turtle.left(10)

def clear():
    turtle.clear()

# Wait
screen = Screen()

# screen.onkey(fun=move, key="space")
screen.onkey(fun=forward, key="w")
screen.onkey(fun=backward, key="s")
screen.onkey(fun=left, key="a")
screen.onkey(fun=right, key="d")
screen.onkey(fun=clear, key="c")

screen.listen()
screen.exitonclick()
