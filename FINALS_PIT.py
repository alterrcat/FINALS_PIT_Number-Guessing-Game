from tkinter import *
from tkinter import messagebox
import random

number = random.randint(1, 10)
attempts = 0
max_attempts = 5

def check_guess():
    global attempts

    try:
        guess = int(entry.get())
        attempts += 1

        attempts_label.config(
            text=f"Attempts: {attempts}/{max_attempts}"
        )

        if guess == number:
            result_label.config(
                text="Correct! Press Restart to play again.",
                fg="green"
            )
            guess_button.config(state=DISABLED)

        elif guess < number:
            result_label.config(
                text="Too Low!",
                fg="orange"
            )

        else:
            result_label.config(
                text="Too High!",
                fg="red"
            )

        if attempts >= max_attempts and guess != number:
            result_label.config(
                text=f"Game Over! Number was {number}",
                fg="red"
            )
            guess_button.config(state=DISABLED)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Enter a valid number"
        )

def restart_game():
    global number, attempts

    number = random.randint(1, 10)
    attempts = 0

    attempts_label.config(
        text=f"Attempts: 0/{max_attempts}"
    )

    result_label.config(text="")
    guess_button.config(state=NORMAL)

    entry.delete(0, END)

root = Tk()
root.title("Number Guessing Game")
root.geometry("350x300")
root.resizable(False, False)
root.configure(bg="#1E1E2F")

title_label = Label(
    root,
    text="Number Guessing Game",
    font=("Helvetica", 18, "bold"),
    bg="#1E1E2F",
    fg="white"
)
title_label.pack(pady=15)

instruction_label = Label(
    root,
    text="Guess a number from 1 to 10",
    font=("Helvetica", 11),
    bg="#1E1E2F",
    fg="#D3D3D3"
)
instruction_label.pack()

entry = Entry(
    root,
    font=("Helvetica", 12),
    justify="center",
    width=15
)
entry.pack(pady=10)

guess_button = Button(
    root,
    text="Guess",
    font=("Helvetica", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    width=12,
    command=check_guess
)
guess_button.pack(pady=5)

restart_button = Button(
    root,
    text="Restart",
    font=("Helvetica", 11, "bold"),
    bg="#2196F3",
    fg="white",
    width=12,
    command=restart_game
)
restart_button.pack(pady=5)

result_label = Label(
    root,
    text="",
    font=("Helvetica", 12, "bold"),
    bg="#1E1E2F"
)
result_label.pack(pady=15)

attempts_label = Label(
    root,
    text=f"Attempts: 0/{max_attempts}",
    font=("Helvetica", 10),
    bg="#1E1E2F",
    fg="white"
)
attempts_label.pack()

root.mainloop()
