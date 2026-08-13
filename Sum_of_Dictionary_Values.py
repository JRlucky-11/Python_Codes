print("_"*75)
dict1 = {'a':5, 'b':2, 'c':7, 'd':10, 'e':9}
print("Your Dictionary Values are: ", dict1.values())
print("\t|> Sum of all Values(Sum Function Method): ", sum(dict1.values()))

Total = sum([val for key, val in dict1.items()])
print("\t|> Sum of all Values(For Loop Method): ", Total)
print("_"*75)