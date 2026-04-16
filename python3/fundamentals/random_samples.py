import random
import string

print(random.random())
print(random.randint(1, 20))
print(random.choice([0, 2, 4, 6, 8]))
print(random.choices([0, 2, 4, 6, 8], k=3))
print("string.ascii_letters:", string.ascii_letters)
print("string.ascii_uppercase:", string.ascii_uppercase)
print("string.digits:", string.digits)
print("".join(random.choices(string.ascii_letters + string.digits, k=16)))
