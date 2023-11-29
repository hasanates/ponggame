from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, 0)

    def initial_go(self):

        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x,new_y)


