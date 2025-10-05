import tkinter as tk

window = tk.Tk()
window.title("Mile to Kms & Kms to Miles - Converter")
window.geometry("500x500")

def miles_kms():
    return None

def kms_miles():
    return None

option_label = tk.Label(text="Choose option for Convertion:)")
option_label.place(x=150,y=50)

def radio_used():
    conversion = radio_state.get()
    return conversion

def conversion_button():
    conversion = radio_used()
    if conversion == 1:
        miles = float(entry.get())
        kms = miles * 1.60934
        output_label.config(text=f"{round(kms,2)} Kms")
    if conversion == 2:
        kms = float(entry.get())
        miles = kms / 1.60934
        output_label.config(text=f"{round(miles,2)} Miles")
    
#Variable to hold on to which radio button value is checked.
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Miles To Kms", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Kms To Miles", value=2, variable=radio_state, command=radio_used)
radiobutton1.place(x=200,y=100)
radiobutton2.place(x=200,y=150)

#Entries
entry = tk.Entry(width=10)
#Add some text to begin with
entry.insert(tk.END, string="")
input_value = entry.get()
entry.place(x=100, y=200)


option_label = tk.Button(text="Convert", command=conversion_button)
option_label.place(x=220,y=200)


output_label = tk.Label(text="")
output_label.place(x=400,y=200)


window.mainloop()