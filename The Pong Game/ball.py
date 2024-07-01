from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10
        self.sleep = 0.1

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def deflect(self):
        self.y *= -1

    def bounce(self):
        self.x *= -1
        self.sleep *= 0.9

    def is_out_of_height(self) -> bool:
        if self.ycor() > 280 or self.ycor() < -280:
            return True

        return False

    def is_out_of_screen(self) -> bool:
        if self.xcor() > 380 or self.ycor() < -380:
            return True

        return False

    def reset_all(self):
        self.goto(0, 0)
        self.sleep = 0.1
