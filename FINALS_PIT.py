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

        if guess > 10 or guess < 1:
            result_label.config(
                text="1 to 10 ngani",
                fg="#FFD166"
            )
            entry.delete(0, END)
            return

        attempts += 1

        attempts_label.config(text=f"Attempts: {attempts}/{max_attempts}")

        if guess == number:
            result_label.config(
                text="Yeyy, Correct! Press Restart to play again.",
                fg="#57CC99"
            )
            guess_button.config(state=DISABLED)

        elif guess < number:
            result_label.config(
                text="Aishh...Too Low!",
                fg="#F4A261"
            )

        else:
            result_label.config(
                text="Aigoo...Too High!",
                fg="#E63946"
            )

        if attempts >= max_attempts and guess != number:
            result_label.config(
                text=f"Game Over! The number was {number}",
                fg="#E63946"
            )
            guess_button.config(state=DISABLED)

        entry.delete(0, END)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number")

def restart_game():
    global number, attempts

    number = random.randint(1, 10)
    attempts = 0

    attempts_label.config(text=f"Attempts: 0/{max_attempts}")
    result_label.config(text="")
    guess_button.config(state=NORMAL)

    entry.delete(0, END)

root = Tk()
root.title("Joefrey Oppa Number Guessing Game")
root.geometry("430x350")
root.resizable(False, False)
root.configure(bg="#22223B")

main_frame = Frame(root, bg="#2B2D42", padx=25, pady=25)
main_frame.pack(expand=True)

title_label = Label(
    main_frame,
    text="Joefrey Oppa Number Guessing Game",
    font=("Century Gothic", 17, "bold"),
    bg="#2B2D42",
    fg="white"
)
title_label.pack(pady=10)

instruction_label = Label(
    main_frame,
    text="Guess a number from 1 to 10",
    font=("Verdana", 10),
    bg="#2B2D42",
    fg="#D9D9D9"
)
instruction_label.pack(pady=5)

entry = Entry(
    main_frame,
    font=("Verdana", 13),
    justify="center",
    width=18,
    relief=FLAT
)
entry.pack(pady=12)

guess_button = Button(
    main_frame,
    text="Guess",
    font=("Verdana", 10, "bold"),
    bg="#57CC99",
    fg="white",
    width=14,
    relief=FLAT,
    cursor="hand2",
    command=check_guess
)
guess_button.pack(pady=6)

restart_button = Button(
    main_frame,
    text="Restart",
    font=("Verdana", 10, "bold"),
    bg="#5390D9",
    fg="white",
    width=14,
    relief=FLAT,
    cursor="hand2",
    command=restart_game
)
restart_button.pack(pady=6)

result_label = Label(
    main_frame,
    text="",
    font=("Verdana", 11, "bold"),
    bg="#2B2D42"
)
result_label.pack(pady=15)

attempts_label = Label(
    main_frame,
    text=f"Attempts: 0/{max_attempts}",
    font=("Verdana", 10),
    bg="#2B2D42",
    fg="#D9D9D9"
)
attempts_label.pack()

root.mainloop()
