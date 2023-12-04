from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(arg=self.l_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=self.r_score, align="center", font=("courier", 80, "normal"))

    def left_score(self):
        self.r_score += 1
        self.clear()

    def right_score(self):
        self.l_score += 1
        self.clear()