import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Tic Tac Toe")

# Track current player (X starts)
current_player = "X"

# Create a 3x3 board (list of buttons)
buttons = [[None for _ in range(3)] for _ in range(3)]

# Function to check for winner
def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            return True
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

# Function to check for draw
def check_draw():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] == "":
                return False
    return True

# Function to handle button click
def on_click(row, col):
    global current_player

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_board()
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the board
def reset_board():
    global current_player
    current_player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""

# Create the buttons and place them in grid
for row in range(3):
    for col in range(3):
        button = tk.Button(window, text="", font=("Arial", 24), width=5, height=2,
                           command=lambda r=row, c=col: on_click(r, c))
        button.grid(row=row, column=col)
        buttons[row][col] = button

# Start the GUI loop
window.mainloop()
