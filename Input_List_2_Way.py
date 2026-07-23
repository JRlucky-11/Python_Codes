# input list for loop
size = int(input("Eneter Size of List:")) # input size of list
list2 = []
list1 = []

# for i in range(0,size): # loop 0 to size..
#     ele = int(input("Enter " + str(i+1) + " Element: ")) # element 1, 2..
#     list1.append(ele) # Add Values
# print("Your list:", list1)

list2 = [int(input("Enter " + str(i+1) + "Element: ")) for i in range(0,size)]
print("Your List: ", list2)