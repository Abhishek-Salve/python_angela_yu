# from turtle import Turtle, Screen
# import resources.day_16_another_module
#
# pen_pointer = Turtle()
# # print(pen_pointer)
#
# my_screen = Screen()    # window in which turtle will show up
# pen_pointer.shape("turtle")
# pen_pointer.color("gold")
#
# pen_pointer.forward(100)
# pen_pointer.circle(100)
# pen_pointer.back(1)
# pen_pointer.circle(100)
#
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon", ["Pikachu", "Charmendar"])
table.add_column("Type", ["Electric", "Fire"])

table.align = "r"

print(table)

