class BankAccount:
    def withdraw(self, amount):
        pass

class SavingsAccount(BankAccount):
    def get_interest(self):
        print("Foiz stavkasi: 5%")

    def withdraw(self, amount):
        print(f"Savings hisobidan {amount}$ yechildi")

class CheckingAccount(BankAccount):
    def get_interest(self):
        print("Foiz stavkasi: 1%")

    def withdraw(self, amount):
        print(f"Checking hisobidan {amount}$ yechildi")
s_a = SavingsAccount()
s_a.get_interest()
s_a.withdraw(3000)

ch_a = CheckingAccount()
ch_a.get_interest()
ch_a.withdraw(2000)
