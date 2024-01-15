# Bhavay Garg
# This class is for the ball

from turtle import Turtle

import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        # ball_y = random.randint(0,15)
        # ball_x = random.randint(0,15)
        # self.goto(x=ball_x , y= ball_y)
        # ball_y = random.randint(-280,280)
        # ball_x = random.choice([-350,350])
        # self.goto(x=ball_x , y= ball_y)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.y_move *= -1
        self.x_move *= -1
        self.move_speed *= 0.9
