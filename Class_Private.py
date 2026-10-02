class Bankacc:
    def __init__(self, balance):
        self.__balance = balance  

    def add_balance(self, amnt):
        if amnt > 0:
            self.__balance += amnt
            print(f"\n${amnt} added successfully.")
        else:
            print("Amount must be greater than 0.")

    def get_balance(self):
        return self.__balance

print("-"* 100)
b1 = Bankacc(1000) # Opening Balance is 1000rs. Private
print(f"Opening Balance is: {b1.get_balance()}$")

print("."* 100)
b1.add_balance(500) # Deposite balance is 500rs.
print(f"Current Balance: {b1.get_balance()}$")
print("-"* 100)