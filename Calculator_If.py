print("\n=========================================")
print("Hello User!")
print("__Welcome to a Calculator Program__")
print("-----------------------------------------")
num1 = int(input("Enter 1st No: "))
num2 = int(input("Enter 2nd No: "))
print("_________________________________________")
print("\t\t[+, -, *, /]")
op = input("Choose Your Operator: ")
if(op == '+'):
    print("You Selected Sum Operator.")
    print ("Your Ans =", num1 + num2)
elif(op == '-'):
    print("You Selected Minus Operaator.")
    print("Your Ans =", num1 - num2)
elif(op == '*'):
    print("You Selected Multiplication Operator.")
    print("Your Ans =", num1 * num2)
elif(op == '/'):
    print("You Selected Divide Operator.")
    print("Your Ans =", num1 / num2)
else:
    print("Please select Valid Operator & run again the program...")
print("=========================================")