dict1 = {'a' : 10, 'b' : 15, 'c' : 20, 'd' : 10, 'e' : 15}
print("Your Dictionary is: ", dict1)

dict2 = {}
list1 = []

for key,value in dict1.items():
    if value in dict2:
        list1 = dict2[value]
        list1.append(key)
    else:
        dict2[value] = [key]
print("Grouped Keys are: ", dict2)