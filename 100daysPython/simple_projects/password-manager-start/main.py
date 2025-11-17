import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(height=200, width=200)
photoimg = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photoimg)
canvas.grid(row=0, column=1)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    # Lists of characters to use in password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Generate random characters
    password_letters = [random.choice(letters) for _ in range(8)]
    password_symbols = [random.choice(symbols) for _ in range(2)]
    password_numbers = [random.choice(numbers) for _ in range(2)]

    # Combine all characters and shuffle
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    
    # Create password string
    password = "".join(password_list)
    
    # Try to copy to clipboard, handle WSL issues
    try:
        pyperclip.copy(password)
    except Exception:
        print(f"Generated password: {password}")  # Fallback: print to console
    
    # Insert password into password entry field
    pass_input.delete(0, tk.END)
    pass_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
         website:{
              "email": email,
              "password": password
         }
    }
    # Check if any fields are empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Warning", message="Please don't leave any fields empty!")
        return      
    # Ask user to confirm details
    is_ok = messagebox.askokcancel(title=website, 
                                     message=f"These are the details entered:\nEmail: {email}"
                                     f"\nPassword: {password}\nIs it ok to save?")    
    # If user confirms, save to file
    try:
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                data = {}
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
                
    except Exception as e:
        messagebox.showinfo(title="Warning", message=f'{e}')    
    
    finally:
            # Clear input fields after saving
            web_input.delete(0, tk.END)
            email_input.delete(0, tk.END) 
            pass_input.delete(0, tk.END)

def search_pass():
    website = web_input.get()
    try:
        with open("data.json", "r") as f:
            json_data = json.load(f)
            if website in json_data:
                email = json_data[website]["email"]
                password = json_data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    except json.JSONDecodeError:
        messagebox.showinfo(title="Error", message="Data file is empty or invalid")

# ---------------------------- UI SETUP ------------------------------- #
web_label = tk.Label(text="Website: ")
email_label = tk.Label(text="Email/Username: ")
pass_label = tk.Label(text="Password: ")

web_input = tk.Entry(width=40)
email_input = tk.Entry(width=40)
pass_input = tk.Entry(width=22)

generate_button = tk.Button(text="Generate Password", width=15, height=1, command=password_gen)
add_button = tk.Button(text="Add To File", width=35, command=save_password)
search_button = tk.Button(text="Search", width=35, command=search_pass)

# Labels aligned to right
web_label.grid(row=1, column=0, sticky="e", padx=5)
email_label.grid(row=2, column=0, sticky="e", padx=5) 
pass_label.grid(row=3, column=0, sticky="e", padx=5)

# Input fields and buttons with proper spacing
web_input.grid(row=1, column=1, sticky="ew", padx=5)
email_input.grid(row=2, column=1, sticky="ew", padx=5)
pass_input.grid(row=3, column=1, sticky="ew", padx=5)

search_button.grid(row=1, column=2, sticky="ew", padx=5)
generate_button.grid(row=3, column=2, sticky="ew", padx=5)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew", padx=5, pady=10)
window.mainloop()