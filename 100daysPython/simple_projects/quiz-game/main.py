import turtle
import pandas as pd
import time


IMAGE = "blank_states_img.gif"
GAME_RUN = True
TOTAL_GUESS = 5
INITIAL_GUESS = 0
SCORE = 0

screen = turtle.Screen()

screen.title("US States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pd.read_csv("50_states.csv")
states_all = data["state"].to_list()


while GAME_RUN:
    user_input = screen.textinput(title=f"{INITIAL_GUESS}/{TOTAL_GUESS} States Correct", prompt="Guess All the City on US Your Guess ⌛: ").title()
    try:
        if user_input == "Exit":
            GAME_RUN = False
            missing_states = [state for state in data.state if state not in data.state]
            new_data = pd.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
        if user_input in data.state.values:
            states_all.remove(user_input)
            INITIAL_GUESS += 1
            SCORE += 1
            if INITIAL_GUESS >= TOTAL_GUESS:
                GAME_RUN = False
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                t.goto(0, 0)
                t.write(f" Game Over! \nFinal Score: {SCORE}/{TOTAL_GUESS} States \n Remaining States Names are Saved in a CSV for reference!!!!", align="center", font=("Arial", 16, "normal"))
                pd.DataFrame(states_all, columns=["remaining_states"]).to_csv("states_to_learn.csv", index=False)
                screen.ontimer(t.clear, 5000)
                break
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == user_input]
            print(state_data)
            t.goto(int(state_data["x"].iloc[0]), int(state_data["y"].iloc[0]))
            t.write(state_data.state.item())
        else:
            INITIAL_GUESS += 1
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.goto(0, 0)
            t.write(f"WRONG GUESS {TOTAL_GUESS - INITIAL_GUESS} Left More !!!", align="center", font=("Arial", 16, "normal"))
            screen.ontimer(t.clear, 1000)
            time.sleep(1)
    except ValueError as e:
        print("ValueError Occurred!")
screen.exitonclick()



