import tkinter as tk
from tkinter import messagebox
import random
import json
import pandas, random, os
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ....................  Functions .........................#

def cross_selected():
    global current_card, timer
    window.after_cancel(timer)
    try:
        current_card = random.choice(to_learn)
    except IndexError:
        messagebox.showinfo(title="Congratulations!", message="You've learned all the words!")
        window.destroy()
        return
    canvas.itemconfig(card_title, text = "French", fill="black")
    canvas.itemconfig(card_word, text = current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    timer = window.after(3000, func=flip_card)

def check_Selected():
    try:
        to_learn.remove(current_card)
        data = pandas.DataFrame(to_learn)
        data.to_csv("data/want_to_learn.csv", index=False)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        cross_selected()
    
def flip_card():
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

# .....................  intiations  ......................#
try:
    data = pandas.read_csv("data/want_to_learn.csv")
except Exception as e:
    data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")


window = tk.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)
canvas = tk.Canvas(height=526, width=800)
card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("arial", 40))
card_word = canvas.create_text(400, 263, text="test", font=("arial", 40))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
cross_image=tk.PhotoImage(file="images/wrong.png")
cross_button = tk.Button(image=cross_image, command=cross_selected)
cross_button.grid(row=1, column=0)
check_image=tk.PhotoImage(file="images/right.png")
check_button = tk.Button(image=check_image, command=check_Selected)
check_button.grid(row=1, column=1)
cross_selected()
window.mainloop()