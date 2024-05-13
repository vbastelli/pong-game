import random
from turtle import Turtle
DIRECTION = random.randint(120, 239)



class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.setheading(0)
        self.dx = 2  # Initial x velocity
        self.dy = 2

    def move_ball(self):
        self.forward(20)

    def bounce_back(self):
        self.dx *= -1
