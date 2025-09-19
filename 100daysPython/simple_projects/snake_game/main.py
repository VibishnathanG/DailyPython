from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.screensize(600, 600)
    screen.tracer(0)
    snake =Snake()
    food = Food()
    score = Score()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    is_game_on = True
    score.display_score()
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        
        if snake.head.distance(food) < 20:
            food.refresh()
            snake.extend()
            score.increase_score()

        if snake.head.xcor() > 580 or snake.head.xcor() < -580 or snake.head.ycor() > 580 or snake.head.ycor() < -580:
            score.reset_score()
            snake.snake_reset()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.reset_score() 
                snake.snake_reset()

    screen.exitonclick()

if __name__ == "__main__":
    main()