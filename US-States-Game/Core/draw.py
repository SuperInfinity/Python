from turtle import Turtle


DATA = ('black', ('Courier', 8, 'bold'))


class Draw(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(DATA[0])

    def jump(self, x, y):
        self.penup()
        self.goto(x, y)
        self.pendown()

    def write_state(self, name, x, y):
        self.jump(x, y)
        self.write(arg=name, font=DATA[1])


