from saving_account import SavingAccount

account = SavingAccount.open()
print(account.default_interest_rate)

account.deposit(10000)
account.withdraw(1000)
print(account.balance)

SavingAccount.default_interest_rate = 0.5
print(account.montly_interest())
    
account.some_prop = 10

print(f"add dynamic some method:", account.some_prop)

another_saving_account = SavingAccount.open()

try:
    print(another_saving_account.some_prop)
except AttributeError as error:
    print("Cannot use method that define dynamically for antoher instance of a class.", error)


someSavingAccount = SavingAccount.open()
anotherSavingAccount = SavingAccount.open()
print(someSavingAccount == anotherSavingAccount)

someSavingAccount.deposit(10000)
print(someSavingAccount > anotherSavingAccount)
print(someSavingAccount < anotherSavingAccount)

anotherSavingAccount.deposit(40000)

print(someSavingAccount + anotherSavingAccount)