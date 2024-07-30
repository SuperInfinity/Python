import time
from turtle import Screen
from paddle import Paddle
import world as wr
from scoreboard import ScoreBoard
from ball import Ball


screen = Screen()
screen.title(wr.TITLE)
screen.setup(width=wr.SCREEN[0], height=wr.SCREEN[1])
screen.bgcolor(wr.SCREEN_COLOR)
screen.tracer(0)
screen.listen()

ball = Ball()

scoreboard = ScoreBoard()

paddle1 = Paddle()
paddle1.goto(wr.A)
paddle2 = Paddle()
paddle2.goto(wr.B)
screen.update()

screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")

game = True

while game:
    time.sleep(ball.sleep)
    screen.update()

    ball.move()

    if ball.is_out_of_height():
        ball.deflect()

    if ball.distance(paddle1) < 45 or ball.distance(paddle2) < 45:
        ball.bounce()

    if ball.xcor() > 380:
        ball.reset_all()
        scoreboard.a_scores()
        scoreboard.write_score()

    elif ball.xcor() < -380:
        ball.reset_all()
        scoreboard.a_scores()
        scoreboard.write_score()

    if scoreboard.score[0] > 10 or scoreboard.score[1] > 10:
        game = False

scoreboard.final_scores()
screen.exitonclick()
