convert_Upper = lambda name: name.upper() 

print("=" * 120)
size = int(input("|> How Many Names?: ")) # input size of list
list2 = []
for i in range(size):
    name = input("\t|> Enter " + str(i+1) + " Name: ")
    list2.append(name)
print("\t\t|>> Your Names Before Converting: ", list2)

print("=" * 120)
list1 = list(map(convert_Upper, list2))
# print("\t\t|>> Your Names After Converting: ", list(map(lambda name: name.upper(), list2)))   <-- It is also workin one line code.
print("\t\t|>> Your Names After Converting: ", list1)
print("=" * 120)