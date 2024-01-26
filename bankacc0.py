class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance,): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if self.balance >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print("-------------")
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

savings = BankAccount (0.5, 1500)
checking = BankAccount (0.3, 6000)

savings.deposit(15).deposit(10).deposit(5).withdraw(30).yield_interest().display_account_info()

checking.deposit(60).deposit(90).deposit(180).withdraw(210).yield_interest().display_account_info()

BankAccount.print_accounts()