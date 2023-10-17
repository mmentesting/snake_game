from turtle import Turtle
import random

COLORS = ["purple1", "red1", "orange1", "yellow1"]

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.penup()
        self.change_position()
        self.change_color()

    def change_position(self):
        x_position = random.randint(-190, 190)
        y_position = random.randint(-190, 190)
        self.setposition(x_position, y_position)

    def change_color(self):
        self.color(random.choice(COLORS))
