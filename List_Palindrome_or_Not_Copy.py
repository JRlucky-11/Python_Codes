print("_____Check This User input list is Palindrome or not!_____")
list1 = []
list1.append(input("|> Enter 1st Element: "))
list1.append(input("|> Enter 2nd Element: "))
list1.append(input("|> Enter 3rd Element: "))
list1.append(input("|> Enter 4th Element: "))
list1.append(input("|> Enter 5th Element: "))
list1.append(input("|> Enter 6th Element: "))

print("\t|>> Your List -> ", list1)

# Palindrome Checking Formula
copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("\t\t>> Your List Follow Palindrome Patten...!")
    print("\t\t>> Yes, This is a Palindrome List.")
else:
    print("\t\t>> No, This is not a Palindrome List.")
