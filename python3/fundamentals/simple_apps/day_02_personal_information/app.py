first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
hight = float(input("Enter your hight: "))
is_marid_txt = input("Are you marid? y/N: ").lower()
if is_marid_txt == "y":
    mariage_status = "marid"
else:
    mariage_status = "single"

print(f"You are {first_name} {last_name} and {age} years old and {mariage_status}.")
if hight >= 195:
    print("You are good for basketball.")
elif 185 >= hight > 195:
    print("You are good for swimming.")
else:
    print("You are a worrier.")
