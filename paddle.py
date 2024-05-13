import turtle
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, pos1, pos2, pos3):
        super().__init__()
        self.starting_pos = [pos1, pos2, pos3]
        self.segments = []
        self.create_paddle()
        self.up()
        self.setheading(UP)
        self.head = self.segments[0]
        self.head.setheading(UP)

    def create_paddle(self):
        for position in self.starting_pos:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)


    def up(self):
        for seg in self.segments:
            seg.setheading(UP)
            seg.forward(20)

    def down(self):
        for seg in self.segments:
            seg.setheading(DOWN)
            seg.forward(20)
