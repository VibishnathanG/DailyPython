
import tkinter as tk
import time
from datetime import datetime

class FlipClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Aesthetic Flip Clock")
        self.root.geometry("400x200")
        self.root.configure(bg='#2E2E2E')
        
        # Create main frame
        self.frame = tk.Frame(self.root, bg='#2E2E2E')
        self.frame.pack(expand=True)
        
        # Create time labels with aesthetic font and colors
        self.time_label = tk.Label(
            self.frame,
            font=('Helvetica', 60, 'bold'),
            bg='#2E2E2E',
            fg='#E8E8E8',
            padx=20
        )
        self.time_label.pack()
        
        # Create date label
        self.date_label = tk.Label(
            self.frame,
            font=('Helvetica', 20),
            bg='#2E2E2E',
            fg='#B8B8B8',
            padx=10
        )
        self.date_label.pack()
        
        # Update time every second
        self.update_time()
        
        self.root.mainloop()
    
    def update_time(self):
        # Get current time and format it
        current_time = datetime.now()
        time_string = current_time.strftime("%H:%M:%S")
        date_string = current_time.strftime("%B %d, %Y")
        
        # Update labels
        self.time_label.config(text=time_string)
        self.date_label.config(text=date_string)
        
        # Create flip animation effect
        self.time_label.update()
        
        # Schedule next update
        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    FlipClock()