from turtle import Turtle, Screen


POSITION_ARG = [(0,0), (-20,0), (-40,0)]
HEAD_SIZE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for segment in POSITION_ARG:
           self.add_Segment(segment) 

    def add_Segment(self, position):
        snake = Turtle()
        snake.color("white")
        snake.shape("square")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_Segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg -1].xcor()
            new_y = self.segments[seg -1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(HEAD_SIZE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)