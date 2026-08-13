def addelemets(*numbers): # single item input [list] *args
    sum1 = 0
    for i in numbers:
        sum1 = sum1 + i
        print("\t\t\t\t", i)
    print("\t\t\t\t=====")
    return sum1

 
size = int(input("|> Enter the number of elements you want to add: "))    # input size of element
numbers = []

for i in range(size): 
    num = int(input(f"|> Enter {i+1} Element: "))  # input Elements
    numbers.append(num)

addallelement = addelemets(*numbers)
print("\t|>> Sum of Values: ", addallelement)