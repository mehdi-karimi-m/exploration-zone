is_continueu = True
while is_continueu:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

    if number < 0:
        break
