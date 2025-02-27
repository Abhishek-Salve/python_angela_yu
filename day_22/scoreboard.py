from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write("Score", align="center", font=("Arial", 15, "normal"))
        self.goto(-200, 270)
        self.write(self.l_score, align="center", font=("Arial", 15, "normal"))
        self.goto(200, 270)
        self.write(self.r_score, align="center", font=("Arial", 15, "normal"))


    def l_score_update(self):
        self.l_score += 1
        self.update_scoreboard()


    def r_score_update(self):
        self.r_score += 1
        self.update_scoreboard()


