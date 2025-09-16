from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen = Screen()
screen.title("Ping Pong")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(key="Up", fun=r_paddle.paddle_up)
screen.onkey(key="Down", fun=r_paddle.paddle_down)
screen.onkey(key="w", fun=l_paddle.paddle_up)
screen.onkey(key="s", fun=l_paddle.paddle_down)

GAME_RUNNING = True
while GAME_RUNNING:
    sleep(0.1)
    screen.update()
    ball.ball_move()

    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.collison_y()
        
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.collison_x()
        ball.increase_speed()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_ball()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_ball()

    if scoreboard.l_score == 5:
        scoreboard.game_over("LEFT PLAYER")
        GAME_RUNNING = False
    elif scoreboard.r_score == 5:
        scoreboard.game_over("RIGHT PLAYER")
        GAME_RUNNING = False

screen.exitonclick()
