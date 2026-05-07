import time
from turtle import Screen

from Pong.ball import Ball
from Pong.paddle import Paddle
from Pong.scoreboard import Scoreboard


screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
l_scoreboard = Scoreboard((-150, 200))
r_scoreboard = Scoreboard((150, 200))

ball = Ball()

screen.listen()

screen.onkey(r_paddle.up ,'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up ,'w')
screen.onkey(l_paddle.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        l_scoreboard.increase_score()
        l_scoreboard.update_scoreboard()

    if ball.xcor() < -380:
        ball.refresh()
        r_scoreboard.increase_score()
        r_scoreboard.update_scoreboard()
screen.exitonclick()