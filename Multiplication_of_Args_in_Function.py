def Multipling(*numbers): # single item input [list] *args
    mul = 1
    for i in numbers:
        mul = mul * i
        print("\t\t\t\t", i)
    print("\t\t\t\t=====")
    return mul

 
size = int(input("|> Enter the number of elements you want to multiply: "))    # input size of element
numbers = []

for i in range(size): 
    num = int(input(f"|> Enter {i+1} Element: "))  # input Elements
    numbers.append(num)

Multiplication1 = Multipling(*numbers)
print("\t|>> Multiplication of Values: ", Multiplication1)