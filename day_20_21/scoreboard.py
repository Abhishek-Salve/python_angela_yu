from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Calibre", 15, "normal")
FILENAME = "data.txt"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.high_score = 0
        self.get_high_score()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(0, 275)
        self.write_score()
        self.hideturtle()


    def write_score(self):
        self.write(arg=f"Score = {self.score}, High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def text_clear(self):
        self.clear()

    def update_score(self):
        self.text_clear()
        self.write_score()

    def increase_score(self):
        self.score = self.score + 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILENAME, "w") as fh:
                fh.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def get_high_score(self):
        with open(FILENAME) as fh:
            self.high_score = int(fh.read())

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"Game Over !", align=ALIGNMENT, font=FONT)