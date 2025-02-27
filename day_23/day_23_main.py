import time
from turtle import Screen
from player import Player, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_gen = CarManager()

screen.onkeypress(key="Up", fun=player.move)
screen.listen()


game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_gen.create_car()
    car_gen.move_cars(scoreboard.level)
    screen.update()

    # Detect if players completes the level
    if player.ycor() > 280:
        scoreboard.level_up()
        player.goto(STARTING_POSITION)

    # Detect player and car collision
    if car_gen.car_collision(player):
        scoreboard.game_over()
        game_is_on = False


# Wait
screen.exitonclick()