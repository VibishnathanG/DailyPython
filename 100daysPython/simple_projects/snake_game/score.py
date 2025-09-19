from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("highscore.txt") as score_f:
                self.high_score = int(score_f.read())
        except ValueError as e:
            print("No Previous Score Found Assuming 0")
            self.high_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.display_score()
    
    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.display_score()
    
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode = "w") as score_file:
                score_file.write(str(self.high_score))
        self.score = 0
        self.display_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))
