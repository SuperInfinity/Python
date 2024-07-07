from turtle import Turtle

LEVEL = 1
FONT = ("Courier", 15, "bold")
X = -260
Y = 260


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = LEVEL
        self.hideturtle()
        self.penup()
        self.goto(X, Y)
        self.pendown()
        self.color("black")
        self.write(arg=f"LEVEL {self.level}", font=FONT)

    def refresh(self):
        self.clear()
        self.penup()
        self.goto(X, Y)
        self.pendown()
        self.write(arg=f"LEVEL {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.refresh()
