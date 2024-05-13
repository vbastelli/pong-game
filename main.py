import turtle
from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle((-280, 0), (-280, 20), (-280, -20))
paddle2 = Paddle((275, 0), (275, 20), (275, -20))
ball = Ball()

turtle.listen()
screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")

screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle1.down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    ball.move_ball()
    if (ball.distance(paddle1) < 50 and ball.xcor() < -260) or (ball.distance(paddle2) < 50 and ball.xcor() > 260):
        ball.bounce_back()
        print('bounce')


screen.exitonclick()
