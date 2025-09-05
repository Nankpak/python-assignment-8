"""
TASK: Create a BankAccount class.

Requirements:
1. Each account should have an owner name and a starting balance.
2. Provide a method to deposit money.
3. Provide a method to withdraw money (only if sufficient balance).
4. Provide a method to check current balance.

Example Usage:
    acc = BankAccount("Alice", 1000)
    acc.deposit(500)
    acc.withdraw(200)
    print(acc.get_balance())  # 1300
"""
class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def deposit(self):
        amount_to_deposit = 500
        if amount_to_deposit <=0:
            print('cannot deposit such amount')
            return 0
        else:
            return self.balance + amount_to_deposit
    def withdraw(self):
        amount_to_withdraw = 200
        if amount_to_withdraw > self.balance:
            print('insufficient fund')
            return 0
        elif amount_to_withdraw <=0:
            print('cannot withdraw such amount')
            return 0
        else:
            if amount_to_withdraw > 0 and amount_to_withdraw <= self.balance:
               return self.balance-amount_to_withdraw
    def show_balance(self):
        print(f'your balance is {self.balance}')
customer1 = BankAccount('alhaji',10000)
print(customer1.balance)
customer1.withdraw()
print(customer1.show_balance())
