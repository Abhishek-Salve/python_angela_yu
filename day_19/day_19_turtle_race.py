from random import randint
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Racing Game")

def forward_turtle(t=None):
    t.forward(randint(1, 10))


t1 = Turtle(shape="turtle")
t1.penup()
t1.color("red")
t1.goto(x=-250, y=-200)

t2 = Turtle(shape="turtle")
t2.penup()
t2.color("green")
t2.goto(x=-250, y=-100)

t3 = Turtle(shape="turtle")
t3.penup()
t3.color("blue")
t3.goto(x=-250, y=0)

t4 = Turtle(shape="turtle")
t4.penup()
t4.color("cyan")
t4.goto(x=-250, y=100)

t5 = Turtle(shape="turtle")
t5.penup()
t5.color("orange")
t5.goto(x=-250, y=200)

x1 = x2 = x3 = x4 = x5 = 0
# y1 = y2 = y3 = y4 = y5 = 0

user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter the color")
print(f"User input is = {user_input.capitalize()}")

winner = None

while 1:
    forward_turtle(t1)
    x1, y1 = t1.position()
    if x1 > 270.0:
        winner = "red"
        break

    forward_turtle(t2)
    x2, y2 = t2.position()
    if x2 > 270.0:
        winner = "green"
        break

    forward_turtle(t3)
    x3, y3 = t3.position()
    if x3 > 270.0:
        winner = "blue"
        break

    forward_turtle(t4)
    x4, y4 = t4.position()
    if x4 > 270.0:
        winner = "cyan"
        break

    forward_turtle(t5)
    x5, y5 = t5.position()
    if x5 > 270.0:
        winner = "orange"
        break

    # print(x1, x2, x3, x4, x5)
    # print(type(x1))
    # print(y1, y2, y3, y4, y5)

# Wait
screen.exitonclick()

if winner == user_input:
    print(f"Your guess '{user_input.capitalize()}' was right. You won !")
else:
    print(f"You guessed wrong. {winner.capitalize()} won !")
