import turtle as t
from turtle import Turtle, Screen
from random import random, randint, choice

turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("orange")
# turtle_direction = ['F', 'L', 'R', 'B']
turtle_direction = [0, 90, 180, 270]


def random_color():
    t.colormode(255)  # changes the color scale from (0.0 - 1.0) to (0, 255)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color



# # # Draw square
# for _ in range(4):
#     turtle.forward(100)
#     turtle.left(90)

# # Draw dashed line
# for _ in range(10):
#     turtle.forward(20)
#     turtle.up()
#     turtle.forward(20)
#     turtle.down()

# # Draw shapes, with random colors
# for side in range(3, 10+1):
#     random_r1 = randint(0, 255) / 256
#     random_g1 = randint(0, 255) / 256
#     random_b1 = randint(0, 255) / 256
#
#     random_r2 = randint(0, 255) / 256
#     random_g2 = randint(0, 255) / 256
#     random_b2 = randint(0, 255) / 256
#
#     turtle.color((random_r1, random_g1, random_b1), (random_r2, random_g2, random_b2))
#     for side_no in range(side):
#         angle = 360/side
#         turtle.forward(100)
#         turtle.left(angle)


# # Draw random walk
# turtle.pensize(10)
# turtle.speed('fastest')
#
# for _ in range(0, 100):
#     random_r1 = randint(0, 255) / 256
#     random_g1 = randint(0, 255) / 256
#     random_b1 = randint(0, 255) / 256
#
#     random_r2 = randint(0, 255) / 256
#     random_g2 = randint(0, 255) / 256
#     random_b2 = randint(0, 255) / 256
#
#     turtle.color((random_r1, random_g1, random_b1), (random_r2, random_g2, random_b2))
#     # turtle.pencolor((random_r1, random_g1, random_b1))
#
#     # dir = choice(turtle_direction)
#     # if dir == 'F':
#     #     turtle.forward(randint(20, 40))
#     # elif dir == 'L':
#     #     turtle.left(90)
#     #     turtle.forward(randint(20, 40))
#     # elif dir == 'R':
#     #     turtle.right(90)
#     #     turtle.forward(randint(20, 40))
#     # else:
#     #     turtle.backward(randint(20, 40))
#
#     turtle.forward(30)
#     turtle.setheading(choice(turtle_direction))


# Draw spirograph
turtle.speed("fastest")

# for tilt in range(0, 360, 90):
#     for angle in range(0, 360):
#         turtle.forward(1)
#         turtle.setheading(angle)
#         turtle.tilt(tilt)

for angle in range(0, 360, 4):
    # turtle.pencolor(random_color())
    r = randint(0, 255) / 256
    g = randint(0, 255) / 256
    b = randint(0, 255) / 256
    turtle.color((r, g, b), (0, 0, 0))

    turtle.circle(100)
    turtle.setheading(angle)


# Wait for user input
screen = Screen()
screen.exitonclick()
