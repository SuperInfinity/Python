from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed(speed="fastest")
        self.goto(x=randint(-280, 280), y=randint(-280, 260))

    def refresh(self):
        self.goto(x=randint(-280, 280), y=randint(-280, 260))
