import time
from snake import Snake
from food import Food
from scoreboard import Score
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.03)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        snake.grow_snake()
        food.refresh()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        # scoreboard.game_over()
        # game_is_on = False
        scoreboard.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()