class SavingAccount:
    default_interest_rate = 0.2

    def __init__(self, initail_balance):
        self.balance = initail_balance

    @classmethod
    def open(cls):
        return cls(0)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount cannot be zero or less.")
        
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("amount cannot be zero or less.")
                
        self.balance -= amount

    def montly_interest(self):
        return self.balance * SavingAccount.default_interest_rate


account = SavingAccount.open()
print(account.default_interest_rate)

account.deposit(10000)
account.withdraw(1000)
print(account.balance)

SavingAccount.default_interest_rate = 0.5
print(account.montly_interest())
    
