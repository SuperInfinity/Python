from turtle import Turtle


FONT = ('Courier', 40, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = [0, 0]
        self.penup()
        self.ht()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.penup()
        self.goto(-60, 220)
        self.pendown()
        self.write(arg=self.score[0], align="center", font=FONT)
        self.penup()
        self.forward(120)
        self.pendown()
        self.write(arg=self.score[1], align="center", font=FONT)

    def a_scores(self):
        self.score[0] += 1

    def b_scores(self):
        self.score[1] += 1

    def final_scores(self):
        self.clear()
        self.penup()
        self.goto(-80, 0)
        self.pendown()
        self.write(arg=f"{self.score[0]} Vs {self.score[1]}", font=FONT)
        self.penup()
        self.goto(-80, -40)
        self.pendown()
        if self.score[0] > self.score[1]:
            self.write(arg="A wins..!", font=FONT)

        else:
            self.write(arg="B wins..!", font=FONT)
