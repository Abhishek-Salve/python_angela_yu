from turtle import Turtle
import time

UPPER_WALL_EDGE = 280
BOTTOM_WALL_EDGE = -280
BALL_SPEED = 0.02

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_direction = 1
        self.y_direction = 1
        self.x_move = 3
        self.y_move = 3
        self.ball_speed = BALL_SPEED


    def move(self):
        curr_xcor = self.xcor()
        curr_ycor = self.ycor()
        # self.goto(curr_xcor + 3  , curr_ycor + 3 )
        self.goto(curr_xcor + (self.x_move * self.x_direction) , curr_ycor + (self.y_move * self.y_direction))


    def wall_collision_detect(self):
        # Detect collision with TOP wall
        if self.ycor() > UPPER_WALL_EDGE:
            self.y_direction = -1

        # Detect collision with BOTTOM wall
        if self.ycor() < BOTTOM_WALL_EDGE:
            self.y_direction = 1


    def paddle_bounce(self):
        self.x_direction *= -1
        self.ball_speed *= 0.9


    def reset_ball(self):
        self.ball_speed = BALL_SPEED
        self.setposition(0, 0)
        self.x_direction *= -1
        time.sleep(0.5)
