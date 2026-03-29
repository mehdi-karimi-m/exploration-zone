number = int(input("enter number: "))

counter = 0
while number > 0:
    if number % 2 == 0:
        print(number)
        counter += 1
    number -= 1

print(f"We have {counter} even numbers.")

print("*" * 20)

evenNumbersInTen = 0
for num in range(1, 10):
    if num % 2 == 0:
        print(num)
        evenNumbersInTen += 1

print(f"We have {evenNumbersInTen} even numbers in 10.")
