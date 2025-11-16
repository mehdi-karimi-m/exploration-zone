import random

roll = random.randint(1, 6)

guess = int(input("Guess the dice roll:\n"))

if roll == guess:
    print("WIN! :-)")
else:
    print("Lose :-(")