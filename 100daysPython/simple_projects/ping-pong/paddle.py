from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x ,y) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x, y)
    
    def paddle_up(self):
        y = self.ycor()
        y += 20
        if y < 300:
            self.sety(y)
        else:
            self.sety(250)

    def paddle_down(self):
        y = self.ycor()
        y -= 20
        if y > -300:
            self.sety(y)
        else:
            self.sety(-250)
        