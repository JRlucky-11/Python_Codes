print("="*60)
a = int(input("|> Enter a number: "))

while True:
    try:
        b = int(input("|> Enter another number: "))
        result = a / b
        break
    except ZeroDivisionError as Error:
        print("\t|>> Your Error is: ", Error, "\n\t|>> Please enter a non-zero number for the second input.\n")

print("-" * 50)
print("|> Result: ", result)
print("=" * 60)