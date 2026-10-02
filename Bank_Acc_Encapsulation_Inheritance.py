class SBAccount:
    def __init__(self, acc_name, acc_no, balance, account_type="SB"):
        self.acc_name = acc_name
        self.acc_no = acc_no
        self._balance = balance
        self._account_type = account_type

    def deposit(self, amount):
        if self._account_type == "FD":
            print("\n\t\t\t\t\t[ERROR] Restricted Access: FD Account Deposit not allowed!")
        else:
            if amount > 0:
                self._balance += amount
                print(f"\t\t\t\t\tSuccessfully Deposited: ₹{amount}")
                print(f"\t\t\t\t\tUpdated Balance: ₹{self._balance}")
            else:
                print("\t\t\t\t\tInvalid Deposit Amount!")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"\t\t\t\t\tSuccessfully Withdrawn: ₹{amount}")
            print(f"\t\t\t\t\tRemaining Balance: ₹{self._balance}")
        else:
            print("\t\t\t\t\tInsufficient balance or invalid amount!")

    def show_details(self):
        print("\n--- ACCOUNT DETAILS ---")
        print(f"\t\t\t\t|> Account Name   : {self.acc_name}")
        print(f"\t\t\t\t|> Account Number : {self.acc_no}")
        print(f"\t\t\t\t|> Account Type   : {self._account_type}")
        print(f"\t\t\t\t|> Current Balance: ₹{self._balance}")
        print("-----------------------")

class FDAccount(SBAccount):
    def __init__(self, acc_name, acc_no, balance):
        SBAccount.__init__(self, acc_name, acc_no, balance, account_type="FD")

print("=== BANK ACCESS SYSTEM ===")
name = input("\t|> Enter Account Name: ")
acc_num = input("\t|> Enter Account Number: ")
initial_bal = float(input("\t|> Enter Initial Balance: "))

print("\n\t|>Select Account Type:")
print("\t\t1. SB Account (Savings Bank - Full Access)")
print("\t\t2. FD Account (Fixed Deposit - Restricted Deposit)")
user_type = input("\t\t|> Enter choice (1/2): ")

if user_type == "1":
    account = SBAccount(name, acc_num, initial_bal)
    print("\n\t\t|>> Logged in as SB ACCOUNT (Savings Bank)")
else:
    account = FDAccount(name, acc_num, initial_bal)  # Calls 2nd Class
    print("\n\t\t>> Logged in as FD ACCOUNT (Fixed Deposit)")


while True:
    print("\n\t\t--- MENU ---")
    print("\t\t1. Deposit Money")
    print("\t\t2. Withdraw Money")
    print("\t\t3. Show Details")
    print("\t\t4. Exit")
    
    choice = input("\t\t\tEnter option (1-4): ")

    if choice == "1":
        amt = float(input("\t\t\t\tEnter Deposit Amount: "))
        account.deposit(amt)

    elif choice == "2":
        amt = float(input("\t\t\t\tEnter Withdrawal Amount: "))
        account.withdraw(amt)

    elif choice == "3":
        account.show_details()

    elif choice == "4":
        print("\nThank you for using Bank System!")
        break

    else:
        print("\t\t\tInvalid choice! Choose between 1 to 4.")