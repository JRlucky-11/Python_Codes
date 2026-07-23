str1 = "! Hello Programmer, Welcome to List Largest Element Searching Operation !" 
print("\n")
print("="* 100)
print(str1.center(100, '='))

size = int(input("|> Eneter Size of List: ")) # input size of list
list1 = [int(input("|> Enter " + str(i+1) + " Element: ")) for i in range(0,size)] # Input Elements 1 by 1
print("|> Your List: ", list1)

smallest = list1[0]
sec_smallest = list1[0]
pos = 0

for i in range(0,len(list1)):
    if(list1[i] < smallest):
        sec_smallest = smallest
        smallest = list1[i]
    elif(list1[i] < sec_smallest and list1[i] != smallest):
        sec_smallest = list1[i]
        pos = i

print("\t|>> Smallest Element: ", smallest)
print("\t|>> 2nd Smallest Element: ", sec_smallest)
print("\t|>> Position of 2nd Smallest Element: ", pos)

print("=Wrong ANswer"* 100)