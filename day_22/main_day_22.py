from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard



# Create the setup main screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

r_paddle = Paddle(1)    # Right player
l_paddle = Paddle(2)    # Left player
screen.tracer(0)

ball = Ball()
scoreboard = ScoreBoard()

# Paddle 1 - movement
screen.onkeypress(key="Up", fun=r_paddle.move_up)
screen.onkeypress(key="Down", fun=r_paddle.move_down)

# Paddle 2 - movement
screen.onkeypress(key="w", fun=l_paddle.move_up)
screen.onkeypress(key="s", fun=l_paddle.move_down)

screen.listen()
game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)

    # Detect wall collision
    ball.wall_collision_detect()

    # Detect collision with right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 360) or (ball.distance(l_paddle) < 50 and ball.xcor() < -360):
        ball.paddle_bounce()

    # Detect out of bounds
    if ball.xcor() > 410:
        scoreboard.l_score_update()
        ball.reset_ball()

    if ball.xcor() < -420:
        scoreboard.r_score_update()
        ball.reset_ball()


# Wait for action
screen.exitonclick()
