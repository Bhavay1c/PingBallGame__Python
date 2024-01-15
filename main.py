# Bhavay Garg
# This class is the main class controlling all the functionality

from turtle import Screen, Turtle
import time
from paddle import Paddles
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("pong")

screen.tracer(0)

paddle_r = Paddles(coordinates=(350,0))
paddle_l = Paddles(coordinates=(-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=paddle_r.up)
screen.onkey(paddle_r.down, "Down")
screen.onkey(key="w", fun=paddle_l.up)
screen.onkey(paddle_l.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #  detect collisions with the wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.hit()

    if ball.distance(paddle_r) > 50 and ball.xcor() > 380:
        ball.home()
        ball.hit()
        scoreboard.l_score_increase()
        ball.move_speed = 0.1

    if ball.distance(paddle_l) > 50 and ball.xcor() < -380:
        ball.home()
        ball.hit()
        scoreboard.r_score_increase()
        ball.move_speed = 0.1



screen.exitonclick()
