num = int(input("Enter num: "))
fact = 1
for i in range(1, num + 1):
    fact = fact * i
    print("\t|>", i, "=", fact)