class Employee:
    def __init__(self, Name, Salary):
        self.Name = Name
        self.Salary = Salary
    
class Developer(Employee):
    def Calculate_Payout(self, bonus):
        return self.Salary + bonus

class Manager(Employee):
    def Calculate_Payout(self, bonus):
        return self.Salary + bonus

d1 = Developer("Alice", 70000)
m1 = Manager("Bob", 90000)
str1 = "CORPORATE PAYROLL SYSTEM"

print("=" * 50)
print(str1.center(50, '-'))
print("_" * 50)
print(f"|> Developer Name: {d1.Name} >> Total Pay: ${d1.Calculate_Payout(12000)} ")
print(f"|> Manager Name: {m1.Name} >> Total Pay: ${m1.Calculate_Payout(10000)}")
print("=" * 50) 