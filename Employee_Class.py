class Employee:
    company_name = "[ Abc Company ]"

    def __init__(self, name, salary, tax_percentage):
        self.name = name
        self._salary = salary
        self._tax_percentage = tax_percentage

    def calculate_tax(self):
        tax_amount = self._salary * (self._tax_percentage / 100)
        salary_after_tax = self._salary - tax_amount
        return tax_amount, salary_after_tax

    def display_details(self):
        tax_amount, After_tax_salary = self.calculate_tax()

        print(Employee.company_name.center(100, '-'))
        print(f"\t|> Employee Name     : {self.name}")
        print(f"\t|> Salary Before Tax : ${self._salary:.2f}")
        print(f"\t|> Tax Percentage    : {self._tax_percentage:.2f} %")
        print(f"\t|> Tax Deducted      : ${tax_amount:.2f}")
        print(f"\t|> After Tax Salary  : ${After_tax_salary:.2f} \n")
        print("-" * 100)

str1 = "( Input Employee Details )"
str2 = "( Processing Employee Payment Salary )"
print(str1.center(100, '='))

while True:
    n = input("|> Enter Employee Name: ")
    if n:
        break
    print("\t\t[!] Invalid Input: Employee name cannot be empty. Please try again.")

while True:
    try:
        s = float(input("|> Enter Main Salary: "))
        if s > 0:
            break
        else:
            print("\t\t[!] Warning: Salary must be greater than 0!")
    except ValueError:
        print("\t\t[!] Error: Invalid input! Please enter salary in numeric format only.")

while True:
    try:
        t = float(input("|> Enter Tax Percentage (%): "))
        if 0 <= t <= 100:
            break
        else:
            print("\t\t[!] Warning: Tax percentage must be between 0 and 100 inclusive!")
    except ValueError:
        print("\t\t[!] Error: Invalid input! Please enter tax percentage in numeric format only.")

emp1 = Employee(n, s, t)

print(str2.center(100, '='))
emp1.display_details()
print("=" * 100)