str1 = "! Hello Programmer, Welcome to List Operation !" 
str2 = "1. Append"
str3 = "2. Clear"
str4 = "3. Copy"
str5 = "4. Count"
str6 = "5. Insert"
str7 = "6. Pop"
str8 = "7. Reverse"
str9 = "8. Sort"
str10 = "! Menu !"

print("\n")
print("="* 100)
print(str1.center(100, '='))
list1 = [1,2,3,4,5,6,7,8,9,10]
print(str10.center(100, '-'))
print("|> Your List => ", list1)
print("", str2, "\n", str3, "\n", str4, "\n", str5, "\n", str6, "\n", str7, "\n", str8, "\n", str9, "\n")

ch = input("Choose Your Option: ")

if(ch == '1'):
    print("\t|>> You Selected Append Option.")
    ap = input("\t|>> Please Input the Character or Number to Append in list -> ")
    if ap.isdigit():
        ap = int(ap)
    list1.append(ap)
    print("\t|>> After Append Your List : ", list1)
elif(ch == '2'):
    print("\t|>> You Selected Clear Option.")
    list1.clear()
    print("\t|>> After Clear Your List : ", list1)
elif(ch == '3'):
    print("\t|>> You Selected Copy Option.")
    copy_list1 = list1.copy()
    print("\t|>> Your 1st List is Copied into a new Variable.[Copy_list1] : ", copy_list1)
elif(ch == '4'):
    print("\t|>> You Selected Count Option.")
    a = input("\t|>> What You can Count -> ")
    if a.isdigit():
        a = int(a)
    print("\t|>> Your Count: ", list1.count(a))
elif(ch == '5'):
    print("\t|>> You Selected Insert Option.")
    idx = int(input("\t|>> Enter index position where you want to insert: "))
    val = input("\t|>> Enter value to insert: ")
    if val.isdigit():
        val = int(val)
    list1.insert(idx, val)
    print("\t|>> After Insert Your List : ", list1)
elif(ch == '6'):
    print("\t|>> You Selected Pop Option.")
    print("\t\t1. Pop by Index")
    print("\t\t2. Pop Last Element")
    pop_ch = input("\t|>> Choose pop type (1 or 2): ")
    if pop_ch == '1':
        idx = int(input("\t|>> Enter index to pop: "))
        removed = list1.pop(idx)
    else:
        removed = list1.pop()
    print("\t|>> Removed Element : ", removed)
    print("\t|>> After Pop Your List : ", list1)
elif(ch == '7'):
    print("\t|>> You Selected Reverse Option.")
    list1.reverse()
    print("\t|>> After Reverse Your List : ", list1)
elif(ch == '8'):
    print("\t|>> You Selected Sort Option.")
    print("\t\t1. Ascending Order")
    print("\t\t2. Descending Order")
    sort_ch = input("\t|>> Choose sort order (1 or 2): ")
    if sort_ch == '2':
        list1.sort(reverse=True)
    else:
        list1.sort(reverse=False)
    print("\t|>> After Sort Your List : ", list1)
else:
    print("\t|>> Please select Valid Option & run again the program...")

print("="* 100)