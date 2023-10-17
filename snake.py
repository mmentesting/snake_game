from turtle import Turtle

START_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:
    def __init__(self):
        self.s_segments = []
        self.create_snake()
        self.head = self.s_segments[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.shapesize(stretch_wid=0.5, stretch_len=0.5)
        new_segment.color("seagreen")
        new_segment.penup()
        new_segment.setposition(position)
        self.s_segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.s_segments[-1].position())

    def reset_snake(self):
        for seg in self.s_segments:
            seg.setposition(1000, 1000)
        self.s_segments.clear()
        self.create_snake()
        self.head = self.s_segments[0]

    def move(self):
        for segment_index in range(len(self.s_segments) - 1, 0, -1):
            new_x = self.s_segments[segment_index - 1].xcor()
            new_y = self.s_segments[segment_index - 1].ycor()
            self.s_segments[segment_index].setposition(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
