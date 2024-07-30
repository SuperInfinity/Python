from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 15, 'bold')
FILE = "highScore.txt"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.highScore = 0
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.pendown()
        self.refresh()

    def write_score(self):
        self.clear()
        self.penup()
        self.goto(x=0, y=270)
        self.pendown()
        self.write(f"Score : {self.score}, High Score : {self.highScore}", align=ALIGNMENT, font=FONT)

    def add_score_and_display(self):
        self.score += 1
        # replace high score
        if self.highScore < self.score:
            self.highScore = self.score

        self.write_score()

    def game_over_message(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over, Final Score : {self.score}", font=FONT, align=ALIGNMENT)

    def refresh(self):
        self.score = 0
        self.read_highscore()
        self.write_score()

    def write_highscore(self):
        with open(FILE, mode="w") as f:
            f.write(str(self.highScore))

    def read_highscore(self):
        with open(FILE, mode="r") as f:
            self.highScore = int(f.read())
