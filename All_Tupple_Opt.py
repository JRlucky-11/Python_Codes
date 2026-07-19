str1 = "! Hello Programmer, Welcome to Tuple Operation !"
str2 = "1. Count"
str3 = "2. Check Element"
str4 = "3. Sort"
str5 = "4. Check Membership"
str6 = "[..Menu..]"


print("\n")
print("="* 100)
print(str1.center(100, '='))

tup = (1,20,40,3,10,90)

print(str6.center(100, '-'))
print("|> Your Tuple => ", tup)
print("", str2, "\n", str3, "\n", str4, "\n", str5, "\n")

ch = input("Choose Your Option: ")

if(ch == '1'):
    print("\t|>> You Selected Count Option.")
    a = input("\t|>> What You can Count -> ")
    if a.isdigit():
        a = int(a)
    print("\t|>> Your Count: ", tup.count(a))
elif(ch == '2'):
    print("\t|>> You Selected Check Element Option.\n\t\t1. Max Element\n\t\t2. Min Element")
    el = input("\t\t|>>> Please Select: ")
    if(el == '1'):
        print("\t\t\t|>>>> In this Tuple Max Element: ", max(tup))
    elif(el == '2'):
        print("\t\t\t|>>>> In this Tuple Min Element: ", min(tup))
    else:
        print("\t\t\t>>>> Please Select Valid Option & Run Again...!")
elif(ch == '3'):
    print("\t|>> You Selected Sort Option. \n\t\t1. Ascending Order\n\t\t2. Descending Order")
    so = input("\t\t|>>> Please Select: ")
    if(so == '1'):
        print("\t\t\t|>>>> Ascending Order: ", sorted(tup, reverse=False))
    elif(so == '2'):
        print("\t\t\t|>>>> Descending Order: ", sorted(tup, reverse=True))
elif(ch == '4'):
    print("\t|>> You Selected Membership Check Option.")
    print("Your Tuple is -> ", tup)
    m = input("\t\t|>>> What do you Check in this Tuple: ")
    
    if m.isdigit():
        m = int(m)

    if m in tup:
        print("\t\t\t|>>>> Yes, Your Element is Present in this Tuple.")
    else:
        print("\t\t\t|>>>> No, Your Element is Not Present in this Tuple..!")
else:
    print("\t>> Please select Valid Option & run again the program...")

print("="* 100)