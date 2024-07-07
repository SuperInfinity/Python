from turtle import Turtle


MOVE = 10
PLACE = (-60, 0)
END = ("GAME OVER", ('Courier', 20, 'bold'), "POWER UP")
START = (0, -280)


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.color("black")
        self.goto(START)
        self.setheading(90)
        self.dist = MOVE

    def move(self):
        self.goto(x=self.xcor(), y=self.ycor() + self.dist)

    def stop(self):
        self.goto(self.xcor(), self.ycor() - self.dist)

    def game_over(self):
        self.goto(PLACE)
        self.color("black")
        self.pendown()
        self.write(arg=END[0], font=END[1])

    def refresh(self):
        self.goto(START)

    def power_up(self):
        self.dist += 5
