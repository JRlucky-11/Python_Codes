class student:
    collageName = "[...Maharshi Collage of Natural Law...]"
    fullmark = 600

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.marks = {}

    def Add_Mark(self, subjectName, mark):
        self.marks[subjectName] = mark
    
    def calculate_percentage(self, total):
        return (total / student.fullmark) * 100

    def result(self):
        total = sum(self.marks.values())
        percentage = self.calculate_percentage(total)

        print(student.collageName.center(100, '-'))
        print(f"\t|> Student Name: {self.name}")
        print(f"\t|> Roll No: {self.rollno}")

        for sub, mark in self.marks.items():
            print(f"\t\t>> {sub} - {mark}")

        print(f"\t|> Total Marks: {total} / {student.fullmark}")
        print(f"\t|> Percentage : {percentage:.2f} % \n")
        print("-" * 100)

str1 = "( Input Student Details )"
str2 = "( Input Process Completed )"
str3 = "( Enter Marks for 6 Subjects )"
print(str1.center(100, '='))

n = input("|> Enter Name: ")
while True:
    try:
        r = int(input("|> Enter Roll No: "))
        break
    except ValueError:
        print("\t\t[!] Error: Roll No must contain numeric digits only. Please try again.")

s1 = student(n, r)

print(str3.center(100, '='))
for i in range(1, 7):
    while True:
        sub_name = input(f"\t|>> Name of Subject {i}: ")
        if sub_name:
            break
        print("\t\t\t[!] Invalid Input: Subject name cannot be empty. Please try again.")
    while True:
        try:
            full_mark = int(input(f"\t\t|>>> Enter marks for {sub_name}: "))

            if 0 <= full_mark <= 100:
                break
            else:
                print("\t\t\t[!] Warning: Marks must be between 0 and 100 inclusive!")
        except ValueError:
            print("\t\t\t[!] Error: Invalid input! Please enter marks in numeric format only.")
    s1.Add_Mark(sub_name, full_mark)

print(str2.center(100, '='))
s1.result()
print("=" * 100)