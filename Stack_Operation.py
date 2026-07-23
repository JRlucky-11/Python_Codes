str1 = "! Hello Programmer, Welcome to Stack Operation [LIFO] !"
str2 = "1. Push (Add Element)"
str3 = "2. Pop (Remove Element)"
str4 = "3. Peek (View Top Element)"
str5 = "4. Display (All Elements)"
str6 = "5. Exit"
str7 = "! Menu !"

print("="* 120)
print(str1.center(120, '='))

size = int(input("|> Eneter Size of Stack: ")) # input size of list
stack = []
top = -1
ch = 0
value = 0

while(ch != 5):
    print(str7.center(120, '-'))
    print(">", str2)
    print(">", str3)
    print(">", str4)
    print(">", str5)
    print(">", str6)
    print("")

    ch = int(input("|> Enter Option: "))
    print("")

    if(ch == 1):
        print("\t|>> You Selected Push Operation.")
        if (top == size -1):
            print("\t\t|>>> Stack Overflow..!")
        else:
            value = int(input("\t\t|>>> Enter Value to Push: "))
            top = top + 1
            stack.append(value)
            print("\t\t|>>> Pushed Seccessfully.")
    elif(ch == 2):
        print("\t|>> You Selected Pop Operation.")
        if(top == -1):
            print("\t\t|>>> Stack Underflow..!")
        else:
            remove = stack.pop()
            top = top - 1
            print("\t\t|>>> Popped Element: ", remove)
            print("\t\t|>>> Popped Successfully")
    elif(ch == 3):
        print("\t|>> You Selected Peek Operation.")
        if(top == -1):
            print("\t\t|>>> Stack is Empty..!")
        else:
            print("\t\t|>>> Top Element: ", stack[top])
    elif(ch == 4):
        print("\t|>> You Selected Display Operation.")
        if(top == -1):
            print("\t\t|>>> Stack is Empty..!")
        else:
            print("\t\t|>>> Stack Elements: ", stack)
    elif(ch == 5):
        print("\t|>> Exiting....")
    else:
        print("\t|>> Invalid Optiion...! Try Again.")

print("="* 120)