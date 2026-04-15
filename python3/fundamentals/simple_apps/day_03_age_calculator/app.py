from datetime import datetime

year_of_birth = int(input("Enter your year of birth: "))

print(f"You are {datetime.now().year - year_of_birth} years old.")
