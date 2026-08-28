print("~" * 100)
str1 = "[ Welcome to Age Calculator Program ]"
current_year = 2026
print("", str1.center(100, '-'))

while True:
    try:
        year = int(input("|> Please Enter Your Birth Year: "))
        month = int(input("|> Please Enter Your Birth Month(1-12): "))
        day = int(input("|> Please Enter your Birth Date(1-31): "))
        break
    except Exception as e:
        print("\t|>> An unexpected error occurred.")
        print("\t|>> ", e)

print("=" * 100)
dob = (year, month, day)
age = current_year - year
print(f"\t|>> Your DoB: {dob}")
print(f"\t|>> Your Age: {age}")

print("=" * 100)
try:
    if(age < 15):
        print("\t\t|>>> Your Age is less 15.")
        raise ValueError("Access Denied! Minimum age requirement is 15 years.")
    else:
        print("\t\t|>> You can Access it!:)")
finally:
        print("\t|>> [ Age calculation process finished ]")

print("~" * 100)