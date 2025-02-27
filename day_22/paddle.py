from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, num):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        if num == 1:
            self.goto(x=380, y=0)
        else:
            self.goto(x=-385, y=0)
        self.shapesize(stretch_wid=1, stretch_len=5)


    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
