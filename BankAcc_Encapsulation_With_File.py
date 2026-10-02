class BankAcc:
    def __init__(self, acc_name, acc_no, initial_balance, password, mobile_no):
        self.acc_name = acc_name
        self.acc_no = acc_no
        self._balance = initial_balance
        self._password = password
        self.mobile_no = mobile_no

    def check_balance(self):
        return self._balance

    def deposit(self, amnt):
        if amnt > 0:
            self._balance += amnt
            print(f"\t\t\t\t\t\t>> Deposited: ++ {amnt}\n\t\t\t\t\t\t\t>> New balance: {self._balance}")
            return True
        else:
            print("\t\t\t\t\t\t\t[System Alert]-> Deposit amount must be positive.")
            return False  
    def withdraw(self, amnt):
        if amnt > 0:
            if amnt <= self._balance:
                self._balance -= amnt
                print(f"\t\t\t\t\t\t>> Withdrawing: --{amnt}\n\t\t\t\t\t\t\t>> New balance: {self._balance}")
                return True
            else:
                print("\t\t\t\t\t\t\t[System Alert]-> Insufficient balance.")
                return False
        else:
            print("\t\t\t\t\t\t\t[System Alert]-> Withdrawal amount must be positive.")
            return False

    def forgot_password(self, new_password):
        self._password = new_password
        print("\t\t\t\t>> Password reset successful! You can now log in with your new password.")

    def display(self):
        print("-" * 150)
        print(f"\t\t\t\t\t|> Account Name: {self.acc_name}")
        print(f"\t\t\t\t\t|> Account Number: {self.acc_no}")
        print(f"\t\t\t\t\t|> Password: {self._password}")
        print(f"\t\t\t\t\t|> Mobile Number: {self.mobile_no}")
        print(f"\t\t\t\t\t|> Balance: {self._balance}")
        print("-" * 150, "\n")


def update_file_balance(target_acc_name, target_acc_no, new_balance):
    # Helper function to keep file balance synced with transactions.
    try:
        with open("Bank_Account.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        updated_lines = []
        current_match = False

        for i, line in enumerate(lines):
            if f"|> Account Name: {target_acc_name}" in line:
                if i + 4 < len(lines) and f"|> Account Number: {target_acc_no}" in lines[i + 1]:
                    current_match = True

            if current_match and "|> Balance:" in line:
                line = f"|> Balance: {new_balance}\n"
                current_match = False
            updated_lines.append(line)

        with open("Bank_Account.txt", "w", encoding="utf-8") as file:
            file.writelines(updated_lines)
    except Exception as e:
        print(f"\t\t\t[System Alert]-> Syncing balance to file failed: {e}")


user_acc1 = None

str7 = "[ Hello Sir, Welcome to the Bank Account Management System with {Jarvis Style} - State Bank of India ]"
print("~" * 150)
print(str7.center(150, "-"))

while True:
    print("\n1. Sir You can Create a New Bank Account in My System - For New Users.")
    print("2. Sir if Your Account Existing in My System - For existing users.")
    print("3. Exit - To exit the My System.")

    try:
        ch = int(input("\n|> Hello Sir, Enter your choice: "))
    except ValueError:
        print("\t[System Alert]-> Please enter a valid option number (1, 2, or 3).")
        continue

    if ch == 1:
        str8 = "[ Create a New Bank Account!! ]"
        print(str8.center(150, "-"))

        while True:
            try:
                name = input("\n\t|> Sir, Enter Account Name: ").strip()
                if not name:
                    print("\t\t[System Alert]-> Name cannot be empty.")
                elif name.isnumeric():
                    print("\t\t[System Alert]-> Name cannot be numeric.")
                else:
                    break
            except Exception as e:
                print(f"\t\t[Error Found]: {e}")

        while True:
            try:
                acc_no = int(input("\n\t|> Enter Account Number: "))
                if acc_no <= 0:
                    print("\t\t[System Alert]-> Account Number must be a positive integer.")
                else:
                    break
            except ValueError:
                print("\t\t[Error Found]: Please enter a valid integer for Account Number.")

        while True:
            try:
                mob_no = int(input("\n\t|> Sir, Enter 10-Digit Mobile Number: "))
                if len(str(mob_no)) == 10 and mob_no > 0:
                    break
                else:
                    print("\t\t[System Alert]-> Mobile number must be a valid 10-digit positive integer.")
            except ValueError:
                print("\t\t[Error Found]: Please enter valid digits for Mobile Number.")

        while True:
            try:
                ps = int(input("\n\t|> Sir, Enter Your Account Password to Remember: "))
                if ps <= 0:
                    print("\t\t[System Alert]-> Password must be a positive integer.")
                else:
                    break
            except ValueError as v:
                print(f"\t\t[Error Found]: {v}")

        while True:
            try:
                print("\n\t|> Sir, Please Select Your Deposite Mode: 'O' for Online or 'C' for Cash")
                ch_dep = input("\n\t\t|> Sir, Please Enter your choice (O/C): ").strip().upper()
                if ch_dep in ['O', 'C']:
                    initial_balance = float(input("\n\t\t|> Sir, Enter Your First Deposite Balance: "))
                    if initial_balance < 0:
                        print("\t\t\t[System Alert]-> Initial Balance cannot be negative.")
                    else:
                        break
                else:
                    print("\t\t[System Alert]-> Invalid choice. Please select 'O' or 'C'.")
            except ValueError:
                print("\t\t[Error Found]: Please enter a valid numerical value for balance.")

        user_acc1 = BankAcc(name, acc_no, initial_balance, ps, mob_no)

        try:
            with open("Bank_Account.txt", "a", encoding="utf-8") as file:
                file.write(f"|> Account Name: {user_acc1.acc_name}\n")
                file.write(f"|> Account Number: {user_acc1.acc_no}\n")
                file.write(f"|> Mobile Number: {user_acc1.mobile_no}\n")
                file.write(f"|> Password: {user_acc1._password}\n")
                file.write(f"|> Balance: {user_acc1._balance}\n")
                file.write("-" * 40 + "\n")

            print("\n\t|> Sir, Please Check Your Details...")
            user_acc1.display()

            str1 = "[ Sir, Your Bank Account Created Successfully. Your details are saved to 'Bank_Account.txt'. ]"
            print(str1.center(150, "-"))

        except IOError as e:
            print(f"\t\t[System Alert]-> File I/O Error: Unable to write data. Details: {e}")
        except Exception as e:
            print(f"\t\t!! Error while saving account details: {e}")

    elif ch == 2:
        str9 = "[ For Existing Customer... ]"
        print(str9.center(150, "-"))

        print("\n\t1. Sir You can Directly Login Your Bank Account - Login.")
        print("\t2. Sir If You cann't Remember Your Password - Forgot Password.")
        print("\t3. Goto - Home")

        try:
            cho = int(input("\n\t|> Sir, Please Enter your Option: "))
        except ValueError:
            print("\t\t[System Alert]-> Please enter digits (1, 2 or 3).")
            cho = 0

        if cho == 1:
            str10 = "[ Sir, You can Login Your Bank Account With Your Name & Password. ]"
            print(str10.center(150, "-"))

            try:
                chk_name = input("\n\t\t\t|> Sir, Enter Your Account Name: ").strip()
                chk_pss = int(input("\t\t\t|> Sir, Enter Your Account Password: "))
            except ValueError:
                print("\t\t\t[System Alert]-> Password must be integer digits only!")
                continue

            login_success = False

            try:
                with open("Bank_Account.txt", "r", encoding="utf-8") as file:
                    lines = file.readlines()

                    saved_name = ""
                    saved_acc_no = 0
                    saved_mob = 0
                    saved_pass = None
                    saved_bal = 0.0

                    for line in lines:
                        try:
                            if "Account Name:" in line:
                                saved_name = line.split("Account Name:")[-1].strip()
                            elif "Account Number:" in line:
                                saved_acc_no = int(line.split("Account Number:")[-1].strip())
                            elif "Mobile Number:" in line:
                                saved_mob = int(line.split("Mobile Number:")[-1].strip())
                            elif "Password:" in line:
                                saved_pass = int(line.split("Password:")[-1].strip())
                            elif "Balance:" in line:
                                saved_bal = float(line.split("Balance:")[-1].strip())

                                if saved_name and saved_pass is not None:
                                    if chk_name == saved_name and chk_pss == saved_pass:
                                        login_success = True
                                        print("")
                                        user_acc1 = BankAcc(saved_name, saved_acc_no, saved_bal, saved_pass, saved_mob)
                                        break
                        except (ValueError, IndexError):
                            continue

            except FileNotFoundError:
                print("\t\t\t[System Alert]-> No 'Bank_Account.txt' file found. Please create an account first.")

            if login_success and user_acc1 is not None:
                str3 = "[ Login Successful! ]"
                print(str3.center(150, "_"))

                while True:
                    str5 = "[ Account Operation Menu ]"
                    print("\n" + str5.center(150, "*"))

                    print("\t\t\t\t1. Balance Enquiry")
                    print("\t\t\t\t2. Deposit Money")
                    print("\t\t\t\t3. Withdraw Money")
                    print("\t\t\t\t4. Display Account Details")
                    print("\t\t\t\t5. Exit")

                    choice = input("\n\t\t\t\t|> Enter your choice (1-5): ").strip()
                    if choice == '1':
                        print(f"\n\t\t\t\t\t|> Current Balance: {user_acc1.check_balance()}")

                    elif choice == '2':
                        try:
                            deposit_amount = float(input("\n\t\t\t\t\t|> Enter amount to deposit: "))
                            if user_acc1.deposit(deposit_amount):
                                update_file_balance(user_acc1.acc_name, user_acc1.acc_no, user_acc1.check_balance())
                        except ValueError:
                            print("\t\t\t\t\t[System Alert]-> Please enter a valid numeric amount for deposit.")

                    elif choice == '3':
                        try:
                            withdraw_amount = float(input("\n\t\t\t\t\t|> Enter amount to withdraw: "))
                            if user_acc1.withdraw(withdraw_amount):
                                update_file_balance(user_acc1.acc_name, user_acc1.acc_no, user_acc1.check_balance())
                        except ValueError:
                            print("\t\t\t\t\t[System Alert]-> Please enter a valid numeric amount for withdrawal.")

                    elif choice == '4':
                        user_acc1.display()

                    elif choice == '5':
                        print("\n\t\t\t\t\t>> Exiting the program. Thank you for using our services!")
                        break

                    else:
                        print("\t\t\t\t[System Alert]-> Invalid choice. Please select a valid option (1-5).")

            else:
                print("\t\t\t\t[System Alert]-> Invalid account name or password. Please try again.")

        elif cho == 2:
            str11 = "[ Reset Password Facility ]"
            print(str11.center(150, "-"))

            try:
                chk_name = input("\n\t\t\t|> Sir, Enter Your Account Name: ").strip()
                chk_mob = int(input("\t\t\t|> Sir, Enter Registered 10-Digit Mobile Number: "))

                account_found = False

                try:
                    with open("Bank_Account.txt", "r", encoding="utf-8") as file:
                        lines = file.readlines()

                    saved_name = ""
                    saved_mob = 0

                    for line in lines:
                        if "Account Name:" in line:
                            saved_name = line.split("Account Name:")[-1].strip()
                        elif "Mobile Number:" in line:
                            saved_mob = int(line.split("Mobile Number:")[-1].strip())

                            if chk_name == saved_name and chk_mob == saved_mob:
                                account_found = True
                                break

                    if account_found:
                        while True:
                            try:
                                new_pass = int(input("\n\t\t\t|> Sir, Enter New Password (Digits Only): "))
                                if new_pass > 0:
                                    break
                                else:
                                    print("\t\t\t[System Alert]-> Password must be a positive integer.")
                            except ValueError:
                                print("\t\t\t[System Alert]-> Password must be digits only!")

                        updated_lines = []
                        current_match = False

                        for i, line in enumerate(lines):
                            if "|> Account Name:" in line:
                                current_match = False
                                record_name = line.split("Account Name:")[-1].strip()

                                if record_name == chk_name and i + 2 < len(lines):
                                    mobile_line = lines[i + 2]
                                    if "|> Mobile Number:" in mobile_line:
                                        record_mob = int(mobile_line.split("Mobile Number:")[-1].strip())
                                        if record_mob == chk_mob:
                                            current_match = True

                            if current_match and "|> Password:" in line:
                                line = f"|> Password: {new_pass}\n"
                                current_match = False

                            updated_lines.append(line)

                        with open("Bank_Account.txt", "w", encoding="utf-8") as file:
                            file.writelines(updated_lines)

                        print("\t\t\t>> Password updated successfully!")
                    else:
                        print("\t\t\t[System Alert]-> Details mismatched! Account Name or Mobile number invalid.")

                except FileNotFoundError:
                    print("\t\t\t[System Alert]-> No 'Bank_Account.txt' file found.")

            except ValueError:
                print("\t\t\t[System Alert]-> Invalid Mobile Number entered.")

        elif cho == 3:
            continue

    elif ch == 3:
        print("")
        print("[ Thank you Sir, for using Jarvis Style Banking System! ]".center(150, "="))
        break

print("~" * 150)