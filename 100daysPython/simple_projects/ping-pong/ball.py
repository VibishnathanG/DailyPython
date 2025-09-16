from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.shapesize(1, 1)
        self.speed("slow")
        self.x_move = 10
        self.y_move = 10

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    def collison_y(self):
        self.y_move *= -1
    
    def collison_x(self):
        self.x_move *= -1
    
    def reset_ball(self):
        self.goto(0, 0)
        self.collison_x()

    def increase_speed(self):
        self.x_move *= 1.1
        self.y_move *= 1.1
