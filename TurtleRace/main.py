from turtle import Turtle, Screen
import random

color = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
turtles = ['a', 'b', 'c', 'd', 'e', 'f']
my_screen = Screen()
my_screen.setup(width=500, height=400)
winner = "Noone"

print(my_screen.window_height())

d = -150
for i in range(len(turtles)):
    turtles[i] = Turtle()
    turtles[i].penup()
    turtles[i].shape('turtle')
    turtles[i].color(color[i])
    turtles[i].setposition(x=-250, y=d + (50 * i))


guess = my_screen.textinput('Prompt', 'Enter ur Guess? (red/green/blue/yellow): ')
key = False

while True:
    for t in my_screen.turtles():
        t.forward(random.randint(0, 20))
        if t.xcor() >= 250:
            winner = t
            key = True
            break
    if key:
        break


if winner.color()[0] == guess:
    print("Wou win..!!!")
else:
    print(f"Winner is {winner.color()[0]}")
    print("You Lose..!!!")

my_screen.exitonclick()
