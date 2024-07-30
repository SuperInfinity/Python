import time
from turtle import Screen
from player import Player
from cars import Car
from scoreboard import ScoreBoard


MAX_CAR = 15
CRASH_DISTANCE = 25
SLEEP = 0.1


# Screen declarations
screen = Screen()
screen.setup(height=600, width=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

# Turtle declaration
player = Player()
screen.onkey(player.move, "Up")
screen.onkey(player.stop, "Down")

# Scoreboard
scoreboard = ScoreBoard()

# Game var.
game = True

# Car
cars = []
for _ in range(MAX_CAR):
    cars.append(Car())

print(cars)

while game:
    time.sleep(SLEEP)
    screen.update()

    # Iterating Cars
    for c in cars:
        c.move()

        if c.xcor() < -300:
            c.refresh()

        if c.distance(player) < 20:
            player.game_over()
            game = False
            break

        if player.ycor() >= 280:
            for car in cars:
                car.increase_speed()

            player.power_up()
            player.refresh()
            scoreboard.increase_level()


screen.exitonclick()
