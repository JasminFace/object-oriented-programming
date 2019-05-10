class BankAccount:
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest = interest_rate * 100

    def __str__(self):
        return f"Your balance: ${self.balance} Your interest rate: {self.interest}%"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else: None

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
        else: None

    def gain_interest(self, interest):
        if interest > 0:
            self.balance += self.balance * interest
        else: None

mine = BankAccount(101, 0.12)
print(mine)
mine.deposit(24)
mine.withdraw(26)
mine.gain_interest(0.12)
print(mine)