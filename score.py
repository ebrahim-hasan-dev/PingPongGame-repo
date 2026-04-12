from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.penup()
        self.hideturtle()
        self.score1()
        self.score2()
        

    def score1(self):
        self.color("blue")
        self.goto(-220,270)
        self.pendown()
        self.write(f"Player One : {self.score_1}",font=("Arial",15,"normal"))
        self.penup()

    def score2(self):
        self.color("red")
        self.goto(100,270)
        self.pendown()
        self.write(f"Player Two : {self.score_2}",font=("Arial",15,"normal"))
        self.penup()

    def increase_score1(self):
        self.clear()
        self.score_1 += 1
        self.score1()
        self.score2()

    def increase_score2(self):
        self.clear()
        self.score_2 += 1
        self.score2()
        self.score1()