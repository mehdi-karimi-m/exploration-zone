first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if first_number > second_number:
    print("Maxnumber is", first_number)
elif first_number < second_number:
    print("Maxnumber is", second_number)
else:
    print(f"{first_number} is equal {second_number}")