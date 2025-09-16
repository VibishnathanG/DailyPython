import random
import pyfiglet


def random_number():
    return random.randint(2, 10)

text = "Black Jacks Game"
ascii_logo = pyfiglet.figlet_format(text, font="slant")
print(ascii_logo)


user_selection = [random_number(), random_number()]
computer_selection = [random_number()]


print(f"Your Card:{user_selection}\nComputer Card:{computer_selection}")

computer_selection.append(random_number())
new_draw = input("Enter Y(If need another Card) or N (For closing the draw) :")
if new_draw == 'Y':
    user_selection.append(random_number())
if sum(user_selection) > 21:
    print(f"You lose, Your card total is {sum(user_selection)} and last drawn card is {user_selection.pop()} and Computer Total is {sum(computer_selection)}")
elif (21 - sum(computer_selection)) < (21 - sum(user_selection)):
    print(f"You lose, Your card total is {sum(user_selection)} and last drawn card is {user_selection.pop()} and Computer Total is {sum(computer_selection)}")
else:
    print(f"You win, Your card total is {sum(user_selection)} and last drawn card is {user_selection.pop()} and Computer Total is {sum(computer_selection)}")