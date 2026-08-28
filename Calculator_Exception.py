str1 = "[ Calculator Exception Handling ]"
str2 = "[ Add Operation ]"
str3 = "[ Subtract Operation ]"
str4 = "[ Multiply Operation ]"
str5 = "[ Divide Operation ]"


add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError as Error:
        print("\t|>> Your Error is: ", Error, "\n\t|>> Please enter a non-zero number for the second input.\n")
        return None

print("="*80)
print(str1.center(80, "-"))
print("."*80)

print("\t1. Add\t2. Subtract\t3. Multiply\t4. Divide\t5. Exit")
print("-"*80)

while True:
    try:
        choice = int(input("|> Enter your choice (1-5): "))
        
        if choice == 5:
            print("\t|>> Exiting the Calculator...!")
            break

        if choice in (1, 2, 3, 4):
            if choice == 1:
                print(str2.center(80, "-"))
            elif choice == 2:
                print(str3.center(80, "-"))
            elif choice == 3:
                print(str4.center(80, "-"))
            elif choice == 4:
                print(str5.center(80, "-"))

            a = int(input("\t|>> Enter a number: "))
            b = int(input("\t|>> Enter another number: "))

            if choice == 1:
                result = add(a, b)
            elif choice == 2:
                result = sub(a, b)
            elif choice == 3:
                result = mul(a, b)
            elif choice == 4:
                result = div(a, b)
            
            if result is not None:
                print(f"\t\t|>>> Result: {result}")
                print("."*80, "\n")

        else:
            print("\t|>> Invalid choice. Please enter a number between 1 and 5.\n")
            
    except ValueError as Error:
        print("\t|>> Your Error is: ", Error, "\n\t|>> Please enter a valid number.\n")

print("="*80)