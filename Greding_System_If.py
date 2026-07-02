mark = int(input("|> Enter your marks: "))

if mark >= 90 and mark <= 100:
    print("\t|> Your grade is A+")
elif mark >= 80 and mark < 90:
    print("\t|> Your grade is A")
elif mark >= 70 and mark < 80:
    print("\t|> Your grade is B")
elif mark >= 60 and mark < 70:
    print("\t|> Your grade is C")
elif mark >= 50 and mark < 60:
    print("\t|> Your grade is D")
elif mark < 50 and mark >= 0:
    print("\t|> You are Fail")
else:
    print("\t|> Invalid marks. Please enter a value between 0 and 100.")
