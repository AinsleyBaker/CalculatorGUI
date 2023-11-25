"""
A calculator in python with GUI using Tkinter module that incorporates multiplication and division.
Author: Ainsley Baker
Date: 11/10/2023
"""

import tkinter as tk

# Function to display result
def equal(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

# Function to calculate the result using eval 
def calculate():
    mathstr = entry.get()
    try:
        result = eval(mathstr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error Has Occured")

# Function to allow negative numbers
def negative():
    current = entry.get()
    if current:
        if current[-1] == "+":
            current = current[:-1] + "-"
        elif current[-1] == "-":
            current = current[:-1] + "+"
        elif current[0] == "-":
            current = current[1:]
        else:
            current = "-" + current
    else:
        current = "-"
    entry.delete(0, tk.END)
    entry.insert(0, current)

# Function for button handling
def button_click(text):
    current = entry.get()
    if current == "Error Has Occured":
        entry.delete(0, tk.END)
    if text == "Clear":
        entry.delete(0, tk.END)
    elif text == "+/-":
        negative()
    elif text != "=":
        equal(text)
    else:
        calculate()

# Create Tkinter window 
win = tk.Tk()
win.title("Calculator")

# Create widget to display ext
entry = tk.Entry(win, width=25, font=("Arial", 18), fg="white", bg="black")
entry.grid(row=0, column=0, columnspan=4)

# Creates layout of calculator with specified row and col
CalcLayout = [("Clear", 1, 0), ("+/-", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 2), ("=", 5, 3)
]

# Loops through the layout and creates each button
for text, row, col in CalcLayout:
    if text not in ["0", "Clear"]:
        button = tk.Button(win, text=text, width=8, height=4, command=lambda text=text: button_click(text), font="Arial",  fg="white", bg="black", activebackground="white", activeforeground="black")
        button.grid(row=row, column=col)
    else:
        button = tk.Button(win, text=text, width=8, height=4, command=lambda text=text: button_click(text), font="Arial",  fg="white", bg="black", activebackground="white", activeforeground="black")
        button.grid(row=row, column=col, columnspan=2,  sticky="nsew")

# Runs main loop
win.mainloop()