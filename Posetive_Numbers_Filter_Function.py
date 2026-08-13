print("-"*90)
size = int(input("|> How many Numbers you want to enter?: ")) # input size of list
list2 = []
list2 = [int(input("\t|> Enter " + str(i+1) + " Number: ")) for i in range(0,size)]
print("-"*90)
print("\t|> Your All Numbers are: ", list2)
print("-"*90)

posetive = filter(lambda i: i > 0, list2)
print("\t|> After using filter function Your Positive Numbers are: ", list(posetive))
print("-"*90)