from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.setup(height=600, width=600)
screen.title("Snake Game")
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision With Food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score_and_display()
        snake.extend()

    # Collision With Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.refresh()
        scoreboard.write_highscore()
        scoreboard.refresh()

    # Collision With Tail
    if snake.collision():
        snake.refresh()
        scoreboard.write_highscore()
        scoreboard.refresh()


scoreboard.game_over_message()
screen.exitonclick()
