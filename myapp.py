import tkinter as tk
import random

# ---------------- GAME LOGIC ---------------- #

player_score = 0
computer_score = 0
history = []

def play(user_choice):
    global player_score, computer_score
    all_choice = ["rock", "paper", "scissor"]
    computer_choice = random.choice(all_choice)

    if user_choice == computer_choice:
        result = "It's a Tie 😐"
    elif (user_choice == "rock" and computer_choice == "scissor") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissor" and computer_choice == "paper"):
        result = "You Win 🎉"
        player_score += 1
    else:
        result = "Computer Wins 🤖"
        computer_score += 1

    result_label.config(text=f"You chose {user_choice}\nComputer chose {computer_choice}\n\n{result}")

    score_label.config(text=f"Player: {player_score}    Computer: {computer_score}")

    history.append(f" {result} ")

    history_box.insert(tk.END, history[-1])
    history_box.yview(tk.END)



# ---------------- UI SETUP ---------------- #

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("1920x1082")
window.configure(bg="#121212")

# ---------------- TITLE ---------------- #

title = tk.Label(window, text="Rock Paper Scissors", font=("Segoe UI", 28, "bold"), fg="#00ADB5", bg="#121212")
title.pack(pady=20)


#---------------- SCORE LABEL ---------------- #

score_label = tk.Label(window,
    text="Player: 0    Computer: 0",
    font=("Segoe UI", 14, "bold"),
    fg="#ffffff",
    bg="#121212"
)
score_label.pack(pady=10)

#----------------- HISTORY ---------------- #

history_frame = tk.Frame(window, bg="#1f1f1f")
history_frame.pack(side="right", fill="y", padx=20, pady=20)

history_title = tk.Label(history_frame, text="Match History",
                         font=("Segoe UI", 16, "bold"),
                         fg="#00ADB5", bg="#1f1f1f")
history_title.pack(pady=10)

history_box = tk.Listbox(history_frame, width=25, height=20,
                         bg="#121212", fg="white",
                         font=("Segoe UI", 12),
                         bd=0)
history_box.pack(padx=10, pady=10)


# ---------------- GAME CARD ---------------- #

card = tk.Frame(window, bg="#1f1f1f", bd=0)
card.pack(pady=20, padx=50)

# ---------------- RESULT LABEL ---------------- #

result_label = tk.Label(card, text="Make your move 👇", font=("Segoe UI", 16), fg="white", bg="#1f1f1f", justify="center")
result_label.grid(row=0, column=0, columnspan=3, pady=20)

# ---------------- IMAGES ---------------- #

rock_img = tk.PhotoImage(file=r"C:\Users\HELLO\OneDrive\Desktop\New Project\rock.png")
paper_img = tk.PhotoImage(file=r"C:\Users\HELLO\OneDrive\Desktop\New Project\paper.png")
scissor_img = tk.PhotoImage(file=r"C:\Users\HELLO\OneDrive\Desktop\New Project\scissor.png")

# ---------------- BUTTON STYLE ---------------- #

def create_button(img, col, choice):
    btn = tk.Button(card, image=img, bd=0, bg="#1f1f1f",
                    activebackground="#333333",
                    command=lambda: play(choice))
    btn.grid(row=1, column=col, padx=30, pady=30)

    # Hover glow
    btn.bind("<Enter>", lambda e: btn.config(bg="#00ADB5"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#1f1f1f"))

# ---------------- BUTTONS ---------------- #

create_button(rock_img, 0, "rock")
create_button(paper_img, 1, "paper")
create_button(scissor_img, 2, "scissor")

window.mainloop()
