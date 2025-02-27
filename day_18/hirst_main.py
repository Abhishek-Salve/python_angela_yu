import colorgram
import turtle as t
from turtle import Turtle, Screen
from random import random, randint, choice

# colors = colorgram.extract('spot_painting.PNG', 20)
# print(colors)
# for color in colors:
#     print(color.rgb)

# first_color = colors[0]
# print(first_color)

# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34
# print(rgb, hsl, proportion)
#
# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s


# # Make a list of the tuples
# color_list = []
#
# # for color in colors:
# #     rgb = str(color.rgb)
# #     rgb = rgb.split(',')
# #     # print(rgb, type(rgb))
# #     for item in rgb:
# #         item = item.strip()
# #         item.split('=')
# #         color_list.append(item[2])
# #         print(item)
# #     print(rgb, type(rgb))


# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     color_list.append(color_tuple)
#
# print(color_list)
# color_list = color_list[4:]
# print(color_list)

color_list = [(214, 154, 94), (235, 215, 86), (169, 50, 93), (35, 111, 158), (202, 136, 162), (121, 172, 197), (213, 66, 104), (147, 79, 62), (22, 170, 209), (214, 87, 70), (33, 47, 66), (42, 126, 93), (229, 167, 193), (120, 39, 69), (42, 53, 111), (58, 38, 49)]

turtle = Turtle()

# 10 x 10 dots
# dot size 20
# distance between dots is 50

t.colormode(255)
turtle.penup()
turtle.speed("fastest")
turtle.hideturtle()

turtle.setheading(225)
turtle.forward(250)
turtle.setheading(0)

start_x = turtle.xcor()
start_y = turtle.ycor()

for row  in range(0, 10):

    for column in range(0, 10):
        turtle.dot(20, choice(color_list))
        turtle.forward(50)

    # Set row position for next row
    turtle.setx(start_x)
    turtle.sety(turtle.ycor() + 50)


turtle.setx(start_x)
turtle.sety(start_y)

# Wait for user input
screen = Screen()
screen.exitonclick()
