str1 = "! Hello Programmer, Welcome to List Largest Element Searching Operation !" 
print("\n")
print("="* 100)
print(str1.center(100, '='))

size = int(input("|> Eneter Size of List: ")) # input size of list
list1 = [int(input("|> Enter " + str(i+1) + " Element: ")) for i in range(0,size)] # Input Elements 1 by 1
print("|> Your List: ", list1)

largest = list1[0]
sec_largest = list1[0]
pos = 0

for i in range(0,len(list1)):
    if(list1[i] > largest):
        largest = list1[i]

for i in range(0, len(list1)):
    if(list1[i] > sec_largest and list1[i] != largest):
        sec_largest = list1[i]
        pos = i

print("\t|>> Largest Element: ", largest)
print("\t|>> 2nd Largest Element: ", sec_largest)
print("\t|>> Position of 2nd Largest Element: ", pos)

print("="* 100)