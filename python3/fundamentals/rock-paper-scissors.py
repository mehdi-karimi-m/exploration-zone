import random

computer_choice = random.choice(["paper", "rock", "scissors"])
user_choice = input("What do you play? (paper/rock/scissors)\n")

print("Computer choice:", computer_choice)

if computer_choice == user_choice:
    print("TIE")
elif (user_choice == "paper" and computer_choice == "rock") or (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper"):
    print("You win :-)")
else:
    print("You lose :-(")