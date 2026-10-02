class Person:
    def __init__(self, name):
        self.name = name
    def details(self):
        print(f"Name: {self.name}")

class Student(Person):
    def __init__(self, name, Id):
        Person.__init__(self, name)
        self.Id = Id
    def Student_Details(self):
        print("")
        print(f"\t|> Name: {self.name} \n\t|> ID: {self.Id}")
        print(f"\t|> Full Name: {self.name}-{self.Id}")
        print('-' * 50)

print('=' * 50)

while True:
    try:
        n = input("|> Enter Name: ").strip()
        if not n:
            print("\t\t[!] Invalid Input: Name cannot be empty. Please try again.")
        elif n.isnumeric():
            print("\t\t[!] Invalid Input: Name cannot be a number. Please try again.")
        else:
            break

    except ValueError as v:
        print(f"\t|> Please Enter Valid Input: {v}")

while True:
    try:
        i = int(input("|> Enter ID: "))
        if i > 0:
            break
        else:
            print("\t\t[!] Warning: Student ID must be a positive number!")
    except ValueError as v:
        print(f"\t|> Please Enter Valid Input: {v}")

s1 = Student(n, i)
s1.Student_Details()
print('=' * 50) #