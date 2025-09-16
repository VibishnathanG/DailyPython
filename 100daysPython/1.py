from turtle import Turtle, Screen
import random, time
from simple_projects.snake_game.main import main






# screen = Screen()
# screen.setup(500, 500)
# screen.bgcolor("black")
# screen.title("Simple Color Game")
# dotted = Turtle()
# dotted.penup()
# dotted.hideturtle()
# dotted.speed("fastest")
# start_x = -380
# start_y = -280
# spacing = 50
# for row in range(12):  # Number of rows
#     for col in range(16):  # Number of columns
#         x = start_x + (col * spacing)
#         y = start_y + (row * spacing)
#         dotted.goto(x, y)
#         dotted.dot(20, (random.random(), random.random(), random.random()))
# dotted.hideturtle()
# screen.exitonclick()



# screen = Screen()
# screen.bgcolor("black")
# screen.title("Simple Spiral Game")


# circle = Turtle()
# circle.shape("circle")
# def circlo(gap):
#     for _ in range(int(360/gap)):
#         circle.color(random.random(), random.random(), random.random())
#         circle.circle(100)
#         circle.setheading(circle.heading() + gap)
#         circle.pensize(2)
#         circle.speed("fastest")
#         circle.penup()
#         circle.goto(0, 0) 
#         circle.pendown()
#         # screen.update()
#         # circle.penup()
#         # circle.goto(0, 0)
#         # circle.pendown()
#         # circle.setheading(0)
#         # circle.clear()
#         # circle.reset()
#         # circle.hideturtle()
#         # screen.tracer(0)
#         # screen.update()
#         # screen.tracer(1)
#     screen.exitonclick()
# circlo(10)

# screen.bgcolor("white")
# screen.title("Simple Walk Game")

# man = Turtle()

# angles = [0, 90, 180, 270]
# man = Turtle()
# man.pensize(5)
# man.speed("fast")

# def random_color():
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     return (r, g, b)

# for _ in range(200):
#     # Generate random RGB values between 0 and 1
#     man.color(random_color())
#     man.forward(30)
#     man.setheading(random.choice(angles))
#     # screen.update()
#     # man.penup()









# # Initialize screen and turtle
# screen = Screen()
# screen.title("Simple Turtle Game")
# screen.bgcolor("green")

# player = Turtle()
# player.color("white")
# player.shape("turtle")
# player.penup()

# # Create food
# food = Turtle()
# food.shape("circle")
# food.color("red")
# food.penup()
# food.goto(100, 100)

# # Set score
# score = 0
# score_display = Turtle()
# score_display.color("white")
# score_display.penup()
# score_display.hideturtle()
# score_display.goto(100, 260)
# score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# # Movement functions
# def move_forward():
#     player.forward(10)
    
# def move_backward():
#     player.backward(10)
    
# def turn_left():
#     player.left(10)
    
# def turn_right():
#     player.right(10)

# # Key bindings
# screen.listen()
# screen.onkey(move_forward, "Up")
# screen.onkey(move_backward, "Down")
# screen.onkey(turn_left, "Left")
# screen.onkey(turn_right, "Right")

# # Main game loop
# while True:
#     screen.update()
    
#     # Check for collision with food
#     if player.distance(food) < 15:
#         food.goto(randint(-290, 290), randint(-290, 290))
#         score += 1
#         score_display.clear()
#         score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# screen.mainloop()
