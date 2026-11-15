
import tkinter as tk
import random

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("600x500")
root.configure(bg="#202A44")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 24, "bold"),
    bg="#202A44",
    fg="white"
)
title.pack(pady=25)

# Instructions
instruction = tk.Label(
    root,
    text="Choose your move!",
    font=("Arial", 15),
    bg="#202A44",
    fg="#F1C40F"
)
instruction.pack(pady=10)

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Score variables
player_score = 0
computer_score = 0

# Result display
result_label = tk.Label(
    root,
    text="Make your choice to start!",
    font=("Arial", 16, "bold"),
    bg="#202A44",
    fg="white"
)
result_label.pack(pady=25)

# Score display
score_label = tk.Label(
    root,
    text="Player: 0     Computer: 0",
    font=("Arial", 16, "bold"),
    bg="#202A44",
    fg="#2ECC71"
)
score_label.pack(pady=10)


# Game function
def play(player_choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(
        text=f"You: {player_choice} | Computer: {computer_choice}\n{result}"
    )

    score_label.config(
        text=f"Player: {player_score}     Computer: {computer_score}"
    )


# Buttons
button_frame = tk.Frame(root, bg="#202A44")
button_frame.pack(pady=20)

rock_button = tk.Button(
    button_frame, text="🪨 Rock",
    font=("Arial", 14, "bold"),
    width=10, command=lambda: play("Rock"),
    bg="#3498DB", fg="white"
)
rock_button.grid(row=0, column=0, padx=8)

paper_button = tk.Button(
    button_frame, text="📄 Paper",
    font=("Arial", 14, "bold"),
    width=10, command=lambda: play("Paper"),
    bg="#9B59B6", fg="white"
)
paper_button.grid(row=0, column=1, padx=8)

scissors_button = tk.Button(
    button_frame, text="✂ Scissors",
    font=("Arial", 14, "bold"),
    width=10, command=lambda: play("Scissors"),
    bg="#E67E22", fg="white"
)
scissors_button.grid(row=0, column=2, padx=8)


# Reset function
def reset_game():
    global player_score, computer_score

    player_score = 0
    computer_score = 0

    result_label.config(text="Make your choice to start!")
    score_label.config(text="Player: 0     Computer: 0")


# Reset button
reset_button = tk.Button(
    root,
    text="RESET GAME",
    font=("Arial", 12, "bold"),
    width=15,
    command=reset_game,
    bg="#E74C3C",
    fg="white"
)
reset_button.pack(pady=20)


# Start application
root.mainloop()
