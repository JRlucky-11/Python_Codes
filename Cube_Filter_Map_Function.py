print("="*100)
size = int(input("|> How manny Numbers you want to input?: ")) # input size of list
list2 = []
list2 = [int(input("\t|> Enter " + str(i+1) + " Number: ")) for i in range(0,size)]
print("\t|> Your all Numbers are: ", list2)
print("-"*100)

even_num = filter(lambda i: i % 2 == 0, list2)
print("\t\t|>> Your Even Numbers in list: ", list(even_num))
print("-"*100)

odd_num = filter(lambda i: i % 2 != 0, list2)
print("\t\t|>> Your Odd Numbers in list: ", list(odd_num))

cube_num = map(lambda num: num ** 3, list2)
print("\t\t\t|>>> Your Cube Number is: ", list2)
print("\t\t\t|>>> Your Cube is: ", list(cube_num))
print("="*100)