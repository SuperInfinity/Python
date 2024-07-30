from turtle import Turtle, Screen

MOVE = 20
ANGLE = 90
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        self.snake = []

        for i in range(3):
            t1 = Turtle('square')
            t1.penup()
            t1.setposition(x=-20 * i, y=0)
            t1.color('white')
            self.snake.append(t1)

        self.head = self.snake[0]

    def extend(self):
        self.create_seg()
        self.snake[-1].setposition(x=self.snake[-2].xcor(), y=self.snake[-2].ycor())

    def create_seg(self):
        t1 = Turtle('square')
        t1.penup()
        t1.setposition(x=-20, y=0)
        t1.color('white')
        self.snake.append(t1)

    def collision(self):
        for seg in self.snake[2:]:
            if self.head.distance(seg) < 20:
                return True

        return False

    def move(self):
        for index in range(len(self.snake) - 1, 0, -1):
            self.snake[index].setposition(x=self.snake[index - 1].xcor(), y=self.snake[index - 1].ycor())
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.snake[0].setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def refresh(self):
        for s in self.snake:
            s.goto(1000, 1000)

        self.snake.clear()

        for i in range(3):
            t1 = Turtle('square')
            t1.penup()
            t1.setposition(x=-20 * i, y=0)
            t1.color('white')
            self.snake.append(t1)

        self.head = self.snake[0]
