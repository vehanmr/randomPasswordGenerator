import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())

        if 8 <= length <= 50:
            password = generate_password(length)
            password_var.set(password)
            copy_button.config(state="normal")  # Enable the copy button
        else:
            messagebox.showerror("Error", "Invalid password length. Please enter a value between 8 and 50.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")

def clear_password():
    password_var.set("")
    copy_button.config(state="disabled")  # Disable the copy button

def copy_to_clipboard():
    password = password_var.get()
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")
    clear_password()

# Create main window
window = tk.Tk()
window.title("Password Generator")

# Set window icon
window.iconbitmap("password.ico")  # Replace "icon.ico" with the actual filename of your icon

# Set minimum window size
window.minsize(310, 120)

# Disable window resizing
window.resizable(False, False)

# Create and pack widgets
f1 = ttk.Frame(window)
f1.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

length_label = ttk.Label(f1, text="Password Length:  ")
length_label.grid(row=0, column=0)

length_entry = ttk.Entry(f1, width=5)
length_entry.grid(row=0, column=1)

generate_button = ttk.Button(window, text="Generate Password", command=generate_and_display_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

f2 = ttk.Frame(window)
f2.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

password_var = tk.StringVar()
password_label = ttk.Label(f2, text="Generated Password: ")
password_label.grid(row=0, column=0)

password_entry = ttk.Entry(f2, textvariable=password_var, state="readonly", width=30)
password_entry.grid(row=0, column=1)

copy_button = ttk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=3, column=0, pady=10, columnspan=2)

clear_button = ttk.Button(window, text="Clear Password", command=clear_password)
clear_button.grid(row=4, column=0, pady=10, columnspan=2)

# Initially disable the copy button
copy_button = ttk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, state="disabled")
copy_button.grid(row=3, column=0, pady=10, columnspan=2)

# Center the window content
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Use a try-except block to catch the FileNotFoundError if the icon file is not found
try:
    # Set the icon for message boxes
    window.tk.call('wm', 'iconphoto', window._w, tk.PhotoImage(file='icon.ico'))
except tk.TclError:
    pass

# Start the Tkinter event loop
window.mainloop()