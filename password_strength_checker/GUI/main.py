import tkinter as tk
from tkinter import ttk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import checker

# --- Functions ---
def check_password():
    pwd = entry.get()
    result = checker.evaluate_password(pwd)
    suggestions = "\n".join(result["suggestions"])

    feedback = f"Strength: {result['strength']}\n"
    feedback += f"Entropy: {result['entropy']}\n"
    feedback += "Blacklisted: " + ("Yes" if result['is_blacklisted'] else "No") + "\n"
    if suggestions:
        feedback += f"\nSuggestions:\n{suggestions}"
        if result["strength"] != "Strong":
            feedback += f"\nExample: {checker.generate_example_password(pwd)}"

    color = "red" if result['strength'] == "Weak" else "orange" if result['strength'] == "Moderate" else "green"
    result_label.config(text=feedback, foreground=color)

def toggle_password():
    entry.config(show="" if show_var.get() else "*")

# --- GUI Setup ---
root = tk.Tk()
root.title("🔐 Password Strength Checker")
root.geometry("500x400")
root.resizable(False, False)
root.configure(bg="#f4f4f4")

style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 11), padding=6)
style.configure("TLabel", font=("Segoe UI", 11), background="#f4f4f4")

title = ttk.Label(root, text="Enter your password:", font=("Segoe UI", 13, "bold"))
title.grid(row=0, column=0, columnspan=2, pady=(20, 10), padx=20)

entry = ttk.Entry(root, width=35, show="*")
entry.grid(row=1, column=0, padx=20, pady=5, sticky="w")

show_var = tk.BooleanVar()
show_checkbox = ttk.Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password)
show_checkbox.grid(row=1, column=1, sticky="w")

check_btn = ttk.Button(root, text="Check Password Strength", command=check_password)
check_btn.grid(row=2, column=0, columnspan=2, pady=15)

result_label = ttk.Label(root, text="", wraplength=460, justify="left", font=("Segoe UI", 10))
result_label.grid(row=3, column=0, columnspan=2, padx=20, pady=10)

root.mainloop()
