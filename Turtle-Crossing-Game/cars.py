import random
from turtle import Turtle

Y = (-220, 250)
X = 280
FACTOR = 10

COLORS = [
    "red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "gray", "cyan", "magenta",
    "lime", "maroon", "navy", "olive", "teal", "silver", "gold"
]


class Car(Turtle):

    def __init__(self):
        super().__init__("square")
        self.color(random.choice(COLORS))
        self.MOVE_RANGE = [1, 10]
        self.penup()
        self.goto(X, random.randint(Y[0], Y[1]))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.speed = random.randint(self.MOVE_RANGE[0], self.MOVE_RANGE[1])

    def refresh(self):
        self.goto(X, random.randint(Y[0], Y[1]))
        self.color(random.choice(COLORS))

    def move(self):
        self.forward(self.speed)

    def increase_speed(self):
        self.MOVE_RANGE[0] += FACTOR
        self.MOVE_RANGE[1] += FACTOR
        self.speed = random.randint(self.MOVE_RANGE[0], self.MOVE_RANGE[1])
