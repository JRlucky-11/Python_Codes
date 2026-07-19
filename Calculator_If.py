str1 = "[+, -, *, /, **, //]"
str2 = "! Welcome to Calculator  Program !"

print("\n")
print("="* 100)
print(str2.center(100, "_"))
print("|> Hello User!, Please Give me 2 Numbers :)")

num1 = int(input("|> Enter 1st No: "))
num2 = int(input("|> Enter 2nd No: "))

print(str1.center(100, '-'))
op = input("|> Choose Your Operator: ")

if(op == '+'):
    print("\t|>> You Selected Sum Operator.")
    print ("\t|>> Your Ans =", num1 + num2)
elif(op == '-'):
    print("\t|>> You Selected Minus Operaator.")
    print("\t|>> Your Ans =", num1 - num2)
elif(op == '*'):
    print("\t|>> You Selected Multiplication Operator.")
    print("\t|>> Your Ans =", num1 * num2)
elif(op == '/'):
    print("\t|>> You Selected Divide Operator.")
    print("\t|>> Your Ans =", num1 / num2)
elif(op == '**'):
    print("\t|>> You Selected Square Section.")
    print("\t|>> Your 1st num Square =>", num1*num1)
    print("\t|>> Your 2nd num Square =>", num2*num2)
elif(op == '//'):
    print("\t|>> You Selected Floar Devision.")
    print("\t|>> Your Ans: ", num1 // num2)
else:
    print("\t|>> Please select Valid Operator & run again the program...")
    
print("="* 100)