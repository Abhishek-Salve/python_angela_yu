# var = print("Hello")
# print(var)
#
# var = len("Hello")
# print(var)

# def my_function():
#     print("Hello")
#     print("Good bye")
#     print("Good bye 1")
#
# my_function()

def turn_left():
    pass

def at_goal():
    pass

def move():
    pass

def front_is_clear():
    pass

def turn_around():
    turn_left()
    turn_left()

def wall_in_front():
    pass

def wall_on_right():
    pass

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# while not at_goal():
#    while front_is_clear():
#        if not at_goal():
#            move()
#        else:
#            break
#    if wall_in_front():
#        jump()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
        while wall_on_right():
            move()
        turn_right()
        move()
        turn_right()
        while front_is_clear():
            move()
    else:
        print("Check condition")
        break

print("End of loop")
