str1 = "! Hello Programmer, Welcome to Set Operation !"
str2 = "1. Union"
str3 = "2. Intersection"
str4 = "3. Difference"
str5 = "4. Symetric_Deference"
str6 = "5. Copy"
str7 = "6. Remove"
str8 = "7. Pop"
str9 = "! Menu !"

print("\n")
print("="* 100)
print(str1.center(100, '='))

# Set
a = {1,2,3,4}
b = {3,4,5,6}
print(str9.center(100, '-'))
print("|> Your Set A =", a)
print("|> Your Set B =", b)
print("", str2, "\n", str3, "\n", str4, "\n", str5, "\n", str6, "\n", str7, "\n", str8, "\n")

ch = input("Choose Your Option: ")

if(ch == '1'):
    print("\t|>> You Selected Union Operation.")
    print("\t|>> Union Ans:", a.union(b))
elif(ch == '2'):
    print("\t|>> You Selected Intersection Operation.")
    print("\t|>> Intersection Ans:", a.intersection(b))
elif(ch == '3'):
    print("\t|>> You Selected Difference Operation.\n\t\t1. A - B\n\t\t2. B - A")
    di = input("\t\t|>>> Please Select:")
    if(di == '1'):
        print("\t\t\t|>>>> You Selected A - B")
        print("\t\t\t|>>>> A - B Ans:", a.difference(b))
    elif(di == '2'):
        print("\t\t\t|>>>> You Selected B - A")
        print("\t\t\t|>>>> B - A Ans:", b.difference(a))
    else:
        print("\t\t\t>>>> Please Select Valid Option & Run Again..!")
elif(ch == '4'):
    print("\t|>> You Selected Symetric_Difference Option.\n\t\t1. A - B\n\t\t2. B - A")
    sd = input("\t\t|>>> Please Select:")
    if(sd == '1'):
        print("\t\t\t|>>>> You Selected A - B")
        print("\t\t\t|>>>> A - B Ans:", a.symmetric_difference(b))
    elif(sd == '2'):
        print("\t\t\t|>>>> You Selected B - A")
        print("\t\t\t|>>>> B - A Ans:", b.symmetric_difference(a))
    else:
        print("\t\t\t>>>> Please Select Valid Option & Run Again..!")
elif(ch == '5'):
    print("\t|>> You Selected Copy Option.")
    copy_set1 = a.copy()
    print("\t|>> Your 'a' set Copied into a new Variable. [Copy_set1] : ", copy_set1)
    copy_set2 = b.copy()
    print("\t|>> Your 'b' set Copied into a new Variable. [Copy_set2] : ", copy_set2)
elif(ch == '6'):
    print("\t|>> You Selected Remove Option.")
    print("\t|>> In which set do you want to perform the Remove Operation?\n\t\t1. Set A\n\t\t2. Set B")
    sel = input("\t\t|>>> Choose Option:")
    if(sel == '1'):
        print("\t\t\t|>>>> ->...Target Set A...<-")
        print("\t\t\t|>>>> Which Element do you Remove?")
        re1 = int(input("\t\t\t\t|>>>>>Enter Remove Element:"))
        a.remove(re1)
        print("\t\t\t\t|>>>>> After Remove Your Set A:", a)
    elif(sel == '2'):
        print("\t\t\t|>>>> ->...Target Set B...<-")
        print("\t\t\t|>>>> Which Element do you Remove?")
        re2 = int(input("\t\t\t\t|>>>>>Enter Remove Element:"))
        b.remove(re2)
        print("\t\t\t\t|>>>>> After Remove Your Set B:", b)
elif(ch == '7'):
    print("\t|>> You Selected Pop Option.")
    print("\t|>> In which set do you want to perform the POP Operation?\n\t\t1. Set A\n\t\t2. Set B")
    po = input("\t\t|>>> Choose Option:")
    if(po == '1'):
        print("\t\t\t|>>>> ->...Target Set A...<-")
        a.pop()
        print("\t\t\t\t|>>>>> After POP Your Set A:", a)
    elif(po == '2'):
        print("\t\t\t|>>>> ->...Target Set B...<-")
        b.pop()
        print("\t\t\t\t|>>>>> After POP Your Set B:", b)
else:
    print("\t>> Please select Valid Option & run again the program...")

print("="* 100)