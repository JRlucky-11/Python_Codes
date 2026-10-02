class Bankacc:
    def __init__(self, balance):
        self.balance = balance

    def add_balance(self, amnt):
        if amnt > 0:
            self.balance += amnt
            print(f"Amount {self.balance} updated.")

    def get_balance(self):
        return self.balance

b1 = Bankacc(1000)
print("Initial Balance:", b1.balance) # Public

b1.add_balance(500)

b1.balance = 2000
print("Balance:", b1.get_balance())