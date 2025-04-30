# Create a class "BankAccount" with attributes account number and balance. Implement
# methods to deposit and withdraw funds, and a display method to show the account details.
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")