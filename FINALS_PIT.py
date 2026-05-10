from tkinter import *
from tkinter import messagebox
import random

number = random.randint(1, 10)

def check_guess():
    try:
        guess = int(entry.get())

        if guess == number:
            result_label.config(text="Correct!")
        elif guess < number:
            result_label.config(text="Too Low!")
        else:
            result_label.config(text="Too High!")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

root = Tk()
root.title("Number Guessing Game")
root.geometry("300x200")

title_label = Label(root, text="Number Guessing Game", font=("Arial", 14))
title_label.pack(pady=10)

instruction_label = Label(root, text="Guess a number from 1 to 10")
instruction_label.pack()

entry = Entry(root)
entry.pack(pady=5)

guess_button = Button(root, text="Guess", command=check_guess)
guess_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()