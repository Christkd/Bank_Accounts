class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance,): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdrawl(self, amount):
        if self.balance >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print("-------------")
        print(f"Balance: {self.balance}")
        print("-------")
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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)
    
    def command_deposit(self, amount,):
        self.account.deposit(amount)
        return self
    
    def command_withdrawl(self, amount):
        self.account.withdrawl(amount)
        return self

    def user_balance(self):
        print(self.name)
        print(self.email)
        self.account.display_account_info()
        return self

User1 = User("Christian", "Christianc@gmail.com")
User1.command_deposit(50).command_withdrawl(20).user_balance()

User2 = User("Dylan", "Dylan@gmail.com")
User2.command_deposit(80).command_withdrawl(10).user_balance()