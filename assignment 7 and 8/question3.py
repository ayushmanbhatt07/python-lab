# Write a Python program to create a class representing a bank. Include methods for managing
# customer accounts and transactions.
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance=0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = {
                "holder": account_holder,
                "balance": initial_balance
            }
            print(f"Account created for {account_holder}.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            print(f"Deposited {amount}. New balance: {self.accounts[account_number]['balance']}")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                print(f"Withdrew {amount}. New balance: {self.accounts[account_number]['balance']}")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Balance for account {account_number}: {self.accounts[account_number]['balance']}")
        else:
            print("Account not found.")