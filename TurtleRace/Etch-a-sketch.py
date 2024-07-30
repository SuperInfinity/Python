from turtle import Turtle, Screen


tim = Turtle()
my_screen = Screen()


def move():
    tim.forward(10)


def left():
    tim.setheading(tim.heading()+10)


def right():
    tim.setheading(tim.heading()-10)


def back():
    tim.forward(-10)


def clear():
    my_screen.resetscreen()


my_screen.onkey(move, "w")
my_screen.onkey(back, 's')
my_screen.onkey(right, "d")
my_screen.onkey(left, 'a')
my_screen.onkey(clear, 'c')
my_screen.listen()
my_screen.exitonclick()
