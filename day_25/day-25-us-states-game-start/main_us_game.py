import turtle
from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US States Game")
screen.setup(height=600, width=900)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
turtle.speed("fastest")

# # To find the co-ordinates of the states - based on mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

game_is_on = True
total_attempts = 0
correct_guesses = 0
guessed_states = []

df = pandas.read_csv("50_states.csv")
# print(df)  # state, x, y
# state_temp = df[df.state == "Ohio"]
# print(state_temp)
# print(state_temp.x[0])
# print(state_temp.iloc[0].x)
# print(state_temp.iloc[0].y )
# print(state_temp)
# print(csv_data["state"])
# print(type(csv_data["state"]))


while game_is_on:
    user_answer = screen.textinput(title=f"{correct_guesses}/50 states correct", prompt="What's another state name ?")
    total_attempts += 1
    # print(f"User guess {total_attempts} = {user_answer}")

    # Check if user guess is in CSV
    for state in df["state"]:
        if state == user_answer.title():
            if state in guessed_states:
                continue

            guessed_states.append(state)
            correct_guesses += 1

            state_row = df[df.state == state]
            # print(state_row)

            # mark the state name with turtle
            # state_x = state_row.iloc[0, 1]
            state_x = state_row.x.item()
            # state_y = state_row.iloc[0, 2]
            state_y = state_row.y.item()
            # print(state_x, state_y)
            turtle.goto(state_x, state_y)
            turtle.write(f"{state.title()}", align="center", font=("Arial", 8, "normal"))
            turtle.goto(0, 0)

    if user_answer == "exit":
        # Exit condition - Save states to learn
        state_list = df.state.to_list()
        # print(state_list)

        states_to_learn = []
        for state in state_list:
            if state in guessed_states:
                continue
            else:
                states_to_learn.append(state)

        # print(guessed_states)
        # print(states_to_learn)
        # print(len(states_to_learn))

        # with open("states_to_learn.csv", "w") as fh:
        #     for state in states_to_learn:
        #         fh.write(f"{state}\n")

        temp_states = pandas.DataFrame(states_to_learn)
        temp_states.to_csv("states_to_learn2.csv")

        break

    # loop exit condition
    if len(guessed_states) == 50:
        game_is_on = False





# # Wait
# screen.exitonclick()
