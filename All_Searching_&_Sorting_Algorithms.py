str1 = "! Hello Programmer, Welcome to Searching & Sorting Algorithm Operation !" 
str2 = "1. Searching Operations."
str3 = "2. Sorting Operations."
str4 = "! Menu !"


print("\n")
print("="* 100)
print(str1.center(100, '='))

size = int(input("Eneter Size of List: ")) # input size of list
list2 = []
list2 = [int(input("Enter " + str(i+1) + " Element: ")) for i in range(0,size)]
print(str4.center(100, '-'))
print("|> Your List => ", list2)
print("", str2, "\n", str3, "\n")

ch = input("Choose Your Option: ")

if(ch == '1'):
    print("\t|>> You Selected Searching Option.")
    str5 = "1. Binary Search"
    str6 = "2. Linear Search"
    print("\t", str5, "\n\t", str6, "\n")

    choose = input("\t|>> Select Your Option: ")

    if (choose == '1'):
        print("\t\t|>>> You Seleced Binary Search Operation.")
        list2 = sorted(list2)
        print("")
        print("\t\t[...1st Step -> Sorting Your Elements...]")
        print("\t\t\t|>>>> Your List: ", list2)

        print("")
        print("\t\t[...2nd Step -> Searching Element...]")
        target = int(input("\t\t\t|>>>> Enter Your Target to Search: "))
        print("")
        print("\t\t\t\t>>>> Target Locked -> ", target, "<-")

        st_idx = 0
        en_idx = size - 1
        mid_idx = 0
        found = False

        while(st_idx <= en_idx):

            mid_idx = (st_idx + en_idx) // 2
            if(list2[mid_idx] == target):
                print("")
                print("\t\t\t>>>> Target Found at Index: ", mid_idx)
                found = True
                break
            elif(list2[mid_idx] > target):
                en_idx = mid_idx - 1
            else:
                st_idx = mid_idx + 1

        if not found:
            print("\t\t\t>>>> No Value Found in this List...!")
            
    elif (choose == '2'):
            print("\t\t|>>> You Seleced Linear Search Operation.")
            target = int(input("\t\t\t|>>>> Enter Your Target to Search: "))
            print("")
            print("\t\t\t\t>>>> Target Locked -> ", target, "<-")

            found = False
            for i in range(size):
                if(list2[i] == target):
                    print("")
                    print("\t\t\t>>>> Target Found at Index: ", i)
                    found = True
                    break

            if not found:
                print("\t\t\t>>>> No Value Found in this List...!")

elif(ch == '2'):
    print("\t|>> You Selected Sorting Option.")
    str7 = "1. Bubble Sort"
    str8 = "2. Insertion Sort"
    str9 = "3. Selection Sort"
    str10 = "4. Exchange Sort"
    print("\t", str7, "\n\t", str8, "\n\t", str9, "\n\t", str10, "\n")

    choose = input("\t|>> Select Your Option: ")

    if (choose == '1'):
        print("\t\t|>>> You Seleced Bubble Sort Operation.")
        for i in range(size - 1):
            for j in range(size - i - 1):
                if list2[j] > list2[j + 1]:
                    list2[j], list2[j + 1] = list2[j + 1], list2[j]
        print("")
        print("\t\t\t>>>> Sorted List: ", list2)

    elif (choose == '2'):
        print("\t\t|>>> You Seleced Insertion Sort Operation.")
        for i in range(1, size):
            key_val = list2[i]
            j = i - 1
            while j >= 0 and key_val < list2[j]:
                list2[j + 1] = list2[j]
                j -= 1
            list2[j + 1] = key_val
        print("")
        print("\t\t\t>>>> Sorted List: ", list2)

    elif (choose == '3'):
        print("\t\t|>>> You Seleced Selection Sort Operation.")
        for i in range(size):
            min_idx = i
            for j in range(i + 1, size):
                if list2[j] < list2[min_idx]:
                    min_idx = j
            list2[i], list2[min_idx] = list2[min_idx], list2[i]
        print("")
        print("\t\t\t>>>> Sorted List: ", list2)
        
    elif (choose == '4'):
        print("\t\t|>>> You Seleced Exchange Sort Operation.")
        for i in range(size - 1):
            for j in range(i + 1, size):
                if list2[i] > list2[j]:
                    list2[i], list2[j] = list2[j], list2[i]
        print("")
        print("\t\t\t>>>> Sorted List: ", list2)
else:
    print("\t|>> Please select Valid Option & run again the program...")

print("="* 100)