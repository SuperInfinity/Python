import random as r
import colorgram as c_g
from turtle import Turtle, Screen, colormode

X_COR = 480
Y_COR = 405
zz = 275


def main():
    colormode(255)
    t1 = Turtle()
    t1.hideturtle()
    t1.penup()
    t1.speed(speed='fast')
    screen = Screen()
    y = -275
    t1.setposition(-275, y)
    image = c_g.extract('hirst.jpeg', 20)
    color = [(207, 155, 102), (57, 107, 128), (162, 82, 43), (125, 79, 97), (122, 156, 171), (126, 175, 159),
             (195, 142, 39), (226, 198, 130), (188, 89, 109), (191, 131, 145), (14, 44, 57), (53, 38, 19),
             (51, 164, 128), (59, 121, 114), (218, 90, 70), (159, 22, 32)]

    for _ in range(10):
        for _ in range(10):
            t1.dot(20, r.choice(color))
            t1.forward(50)

        y += 50
        t1.setposition(-275, y)

    screen.exitonclick()


def random_colour():
    red = r.randint(0, 255)
    blue = r.randint(0, 255)
    green = r.randint(0, 255)
    color = (red, green, blue)
    return color


def draw_random_walk():
    t2 = Turtle()
    t2.speed(speed='fast')
    t2.width(20)
    colormode(255)
    directions = [0, 90, 180, 270]
    for _ in range(1000):
        t2.forward(50)
        t2.setheading(r.choice(directions))
        t2.pencolor(random_colour())

    Screen().exitonclick()


def random_circle():
    colormode(255)
    my_screen = Screen()
    t3 = Turtle()
    t3.speed(speed='fastest')
    for i in range(0, 360, 4):
        t3.pencolor(random_colour())
        t3.circle(radius=100)
        t3.setheading(i)

    my_screen.exitonclick()
