class Bankacc:
    def __init__(self, balance):
        self._balance = balance

    def add_balance(self, amnt):
        if amnt > 0:
            self._balance += amnt
            print(f"Amount {self._balance} updated.")

    def get_balance(self):
        return self._balance


class SavingsAcc(Bankacc):
    def apply_interest(self, rate):
        interest = self._balance * (rate / 100)
        self._balance += interest
        print()

s= SavingsAcc(1000) # called parrent class(Protected)
s.apply_interest(5)
print(s.get_balance())