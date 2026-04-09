import sys
from pprint import pprint
#import pprint
import sales
from demo_packaging.customer_accounting.account import Account
#from custom_container import TagCounter
#import custom_container

# tagCounter = TagCounter()
# tagCounter.add("Test")

pprint(sys.path)

# amount = int(input("Enter amount: "))
amount = 500

print("Discount:", sales.calculate_discount(amount))
print("Tax:", sales.calculate_tax(amount))
print("-" * 20)
print("Total amount:", sales.calculate_total_amount(amount))

# ==================================== Packages ====================================#

my_account = Account.open(1)

pprint(dir(Account))
print("Account.__name__:", Account.__name__)
print("Account.__module__", Account.__module__)
print("*" * 20)
print("sales__name__:", sales.__name__)
print("sales__package:", sales.__package__)
print("sales__file__:", sales.__file__)
