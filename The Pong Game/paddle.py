from turtle import Turtle


COLOR = "white"
SHAPE = "square"
MOVE = 20


class Paddle(Turtle):

    def __init__(self):
        super().__init__(SHAPE)
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color(COLOR)
        self.penup()

    def up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + MOVE)

    def down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - MOVE)
