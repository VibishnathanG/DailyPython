print("Welcome to the Number Guessing Game:)")

def random_number():
    import random
    return random.randint(1, 100)
guessed_number = random_number()

def level_choose():
    global life
    life = 0
    diff = int(input(f"Enter 1 For Difficuly Level Low(10 Guess) or \n Enter 2 For Difficuly Level Medium(5 Guess) or \n Enter 3 For Difficuly Level High(3 Guess)\n"))
    if diff == 1:
        life = 10
        return life
    elif diff == 2:
        life = 5
        return life
    else:
        life = 3
        return life
total_life = level_choose()
def guess_number():
    global total_life
    while total_life > 0:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < guessed_number:
            print("Too low!")
        elif guess > guessed_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {guessed_number} correctly!")
            return
        total_life -= 1
        print(f"You have {total_life} guesses left.")
    print(f"Sorry, you've run out of guesses. The number was {guessed_number}.")

guess_number()