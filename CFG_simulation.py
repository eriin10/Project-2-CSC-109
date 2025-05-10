from pyparsing import Literal, OneOrMore, StringStart, StringEnd
import tkinter as tk
from tkinter import messagebox

# 2.1: Build CFG parser using pyparsing
# Define terminal symbols
aa = Literal('aa')
bb = Literal('bb')
cc = Literal('cc')

# Define non-terminal patterns with repetition
A = OneOrMore(aa).setResultsName('A')  # A → aa A | aa  (at least one "aa")
C = cc                                # C → cc
B = OneOrMore(bb).setResultsName('B')  # B → B bb | bb  (at least one "bb")

# Define the full grammar: S → A C B, with start and end anchors
grammar = StringStart() + A + C + B + StringEnd()

# 2.2: Define the GUI logic and interaction
def on_submit():
    # Get user input from entry box
    text = entry.get().strip()
    
    # Show the current input above the input box
    input_display.config(text=f"Input: {text}")
    
    try:
        # Try parsing the input using the CFG grammar
        grammar.parseString(text)
        # If parsing succeeds, display ACCEPTED in green
        result_label.config(text="Result: ACCEPTED", fg="green")
    except Exception:
        # If parsing fails, display REJECTED in red
        result_label.config(text="Result: REJECTED", fg="red")
    
    # Clear the input box for the next input
    entry.delete(0, tk.END)


# === GUI SETUP ===

# Create main window
root = tk.Tk()
root.title("CFG Simulator")            # Window title
root.geometry("400x250")              # Window size
root.config(bg="#f0f0f0")             # Background color
root.resizable(False, False)          # Disable resizing

# Title label at the top
title_label = tk.Label(
    root, 
    text="CFG Simulator", 
    font=("Verdana", 14, "bold"), 
    bg="#f0f0f0",
    padx=10, pady=5
)
title_label.pack(pady=10)

# Label that displays the user's most recent input
input_display = tk.Label(
    root, 
    text="Input: ", 
    font=("Verdana", 10), 
    bg="#f0f0f0", 
    fg="#333"
)
input_display.pack(pady=(0, 5))

# Entry box where user types their input string
entry = tk.Entry(
    root, 
    width=30, 
    font=("Verdana", 10)  # Smaller font size
)
entry.pack(pady=(5, 20))  # Adds more space below the entry box

# Define hover effect for the button
def on_enter(e):
    btn['background'] = '#2e7d32'  # Darker green on hover

def on_leave(e):
    btn['background'] = '#4CAF50'  # Default green on leave

# "Check" button to validate input string
btn = tk.Button(
    root, 
    text="Check", 
    command=on_submit, 
    font=("Verdana", 12), 
    bg="#4CAF50", 
    fg="white", 
    padx=10, 
    pady=5
)
btn.bind("<Enter>", on_enter)  # Bind hover-in event
btn.bind("<Leave>", on_leave)  # Bind hover-out event
btn.pack(pady=5)

# Label to show the result (ACCEPTED/REJECTED) below the button
result_label = tk.Label(
    root, 
    text="", 
    font=("Verdana", 12), 
    bg="#f0f0f0"
)
result_label.pack(pady=(15, 15))  # Adds top and bottom spacing

# Start the GUI event loop
root.mainloop()
