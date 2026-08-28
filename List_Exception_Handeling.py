str1 = "! Hello Programmer, Welcome to List Exception Handling !" 
str2 = "1. Append"
str3 = "2. Clear"
str4 = "3. Copy"
str5 = "4. Count"
str6 = "5. Insert"
str7 = "6. Pop"
str8 = "7. Reverse"
str9 = "8. Sort"
str10 = "! Menu !"
str11 = "9. Exit"

append = lambda list1, value: list1.append(value)
clear = lambda list1: list1.clear()
copy = lambda list1: list1.copy()
count = lambda list1, value: list1.count(value)
insert = lambda list1, index, value: list1.insert(index, value)
pop = lambda list1, index=None: list1.pop(index)
reverse = lambda list1: list1.reverse()
sort = lambda list1, reverse=False: list1.sort(reverse=reverse)

print("="* 100)
print(str1.center(100, '='))
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(str10.center(100, '-'))
print("|> Your List => ", list1)
print(f"\t{str2}\n\t{str3}\n\t{str4}\n\t{str5}\n\t{str6}\n\t{str7}\n\t{str8}\n\t{str9}\n\t{str11}\n")
print("="* 100)

while True:
    try:
        ch = int(input("|> Enter your Choice (1-9): "))

        if ch == 1:
            print("\t|>> You Selected Append Option.")
            value = int(input("\t\t|>>> Enter the value to append: "))
            append(list1, value)
            print(f"\t\t\t|>>>> Updated List is: {list1}")

        elif ch == 2:
            print("\t|>> You Selected Clear Option.")
            clear(list1)
            print(f"\t\t|>>> Success! List Cleared. Updated List is: {list1}")

        elif ch == 3:
            print("\t|>> You Selected Copy Option.")
            copied_list = copy(list1)
            print(f"\t\t|>>> Copied List is: {copied_list}")

        elif ch == 4:
            print("\t|>> You Selected Count Option.")
            value = int(input("\t\t|>>> Enter the value to count: "))
            count_value = count(list1, value)
            print(f"\t\t\t|>>>> Count of {value} in List is: {count_value}")

        elif ch == 5:
            print("\t|>> You Selected Insert Option.")
            index = int(input("\t\t|>>> Enter the index to insert at: "))
            value = int(input("\t\t|>>> Enter the value to insert: "))
            insert(list1, index, value)
            print(f"\t\t\t|>>>> Updated List is: {list1}")

        elif ch == 6:
            print("\t|>> You Selected Pop Option.")
            index = int(input("\t\t|>>> Enter the index to pop: "))
            popped_value = pop(list1, index)
            print(f"\t\t\t|>>>> Popped Value is: {popped_value}. Updated List is: {list1}")

        elif ch == 7:
            print("\t|>> You Selected Reverse Option.")
            reverse(list1)
            print(f"\t\t|>>> Reversed List is: {list1}")

        elif ch == 8:
            print("\t|>> You Selected Sort Option.")
            print("\t\t1. Sort in Ascending Order")
            print("\t\t2. Sort in Descending Order")
            sort_choice = int(input("\t\t\t|>>>> Enter your choice (1 or 2): "))
            
            if sort_choice == 2:
                sort(list1, reverse=True)
                print(f"\t\t\t\t|>>>>> Sorted List in Descending Order: {list1}")
            else:
                sort(list1)
                print(f"\t\t\t\t|>>>>> Sorted List in Ascending Order: {list1}")

        elif ch == 9:
            print("\t|>> Exiting the program...")
            break

        else:
            print("\t|>> Invalid choice! Please enter a number between 1 and 9.")

    except ValueError as ve:
        print(f"\t|>> Error: Invalid input! Please enter a valid number. ({ve})")

    except IndexError as ie:
        print(f"\t|>> Error: Index out of range! ({ie})")

    except Exception as e:
        print(f"\t|>> An unexpected error occurred: {e}")

print("="* 100)