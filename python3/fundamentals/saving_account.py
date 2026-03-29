class SavingAccount:
    default_interest_rate = 0.2

    # https://rszalski.github.io/magicmethods/
    def __init__(self, initail_balance):
        self.balance = initail_balance

    def __str__(self):
        return f"Balance: {self.balance}"
    
    def __eq__(self, other):
        return self.balance == other.balance

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
    
    def __gt__(self, other):
        return self.balance > other.balance
    
    def __add__(self, other):
        return self.balance + other.balance