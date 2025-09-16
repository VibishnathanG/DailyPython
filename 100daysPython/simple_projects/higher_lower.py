from os import system
import pyfiglet
import random, time

comparision = {
    "Apple" : 30,
    "Orange" : 40,
    "Mango" : 170,
    "Grapes" : 130,
    "Lichi" : 120,
    "Mosambi" : 20
}

game_status = True
fruit_list = list(comparision.keys())
pending_items = fruit_list.copy()
item1 = random.choice(fruit_list)
pending_items.remove(item1)
score = 0
while game_status:
    system("clear")
    if score:
        print(f"You Are Correct and Your Score Is {score}")
    
    print(pyfiglet.figlet_format("Higher Lower", font="slant"))
    print("Find Which Fruit Has High Cals:>>>")
    item2 = random.choice(pending_items)
    print(f"Which Fruit has high Cal?\nItem - 1 : {item1}")
    print(pyfiglet.figlet_format("VS", font="slant"))
    print(f"Item - 2: {item2}")
    user_choice = input("Type '1' for Item-1 or '2' for Item-2 : ")
    if comparision[item1] > comparision[item2]:
        correct_answer = '1'
        reset = False
    else:
        correct_answer = '2'
        reset = True
    if user_choice == correct_answer:
        score +=1
    else:
        print(f"You Lose wrong Guess !! Actual Value are For {item1} is {comparision[item1]} and {item2} is {comparision[item2]}")
        print(f"Your Final Score Is {score}")
        game_status = False
    if reset:
         item1 = item2
         pending_items.remove(item1)
    else:
         pending_items.remove(item2)
    if not len(pending_items):
        game_status = False

if score >=5:
    print("Congratulations You Won The Game")