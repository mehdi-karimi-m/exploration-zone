name = input("Enter your name: ")
print(f"Your name is {len(name)} characters.")
chars = list(name)
chars.reverse()
reversed_name = ""
for c in chars:
    reversed_name += c

print(reversed_name)

a = ""
for i in range(len(name)):
    a += name[(i + 1) * -1]
print(a)

letter = name.split(" ")

print("Total letters: ", len(letter))