class BankAccount:
    def __init__ (self, account_number,account_user_name,balance):
        self.account_number = account_number
        self.account_user_name = account_user_name
        self.balance = balance
    def deposit(self, amount):
        if amount<0:
            print("Deposit amount must be greater than zero.")
            return
        else:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
    def withdraw(self, amount):
        if amount>self.balance:
            print("needed ammount is more thant the balance.")
            return
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
    def get_balance(self):
        return self.balance
    def get_account_info(self):
        return f"Account Number: {self.account_number}, User Name: {self.account_user_name}, Balance: {self.balance}"