a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num: "))
c = int(input("Enter 3rd num: "))

if (a > b and a > c):
    print("Your 1st num -> ", a, " is Greater.")
elif (b > c):
    print("Your 2nd num -> ", b, " is Greater.")
else:
    print("Your 3rd num -> ", c, "is Greater.")