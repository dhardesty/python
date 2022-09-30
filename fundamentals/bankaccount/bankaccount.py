class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount 
        if (self.balance < 0):
            print(f"Insufficient funds: charging a $5 fee")
        return self

    def display_account_info(self):
        print(f"Interest rate is " + str(self.int_rate))
        print(f"balance is " + str(self.balance))
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += self.balance * self.int_rate
        return self 

adrien_BankAccount = BankAccount (0.2, 200)
lisa_BankAccount = BankAccount (0.4, 500)

adrien_BankAccount.display_account_info()
lisa_BankAccount.display_account_info()

adrien_BankAccount.deposit(50).deposit(50).deposit(50).withdraw(20).yield_interest().display_account_info()
lisa_BankAccount.deposit(100).deposit(100).withdraw(10).withdraw(10).withdraw(10).withdraw(10).yield_interest().display_account_info()
