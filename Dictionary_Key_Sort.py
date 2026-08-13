dict1 = {'h': 3, 'a':6, 't':2, 'y':12, 'p':1, 'e':40} # Unsorted Dictionary
print("|> Unsorted Dictionary: ", dict1)
print("\t|> Sort Dictionary Funtion Method: ", sorted(dict1.items()))

keys1 = list(dict1.keys()) # Convert to List
for i in range(len(keys1)): # Using buble sort concept
    for j in range(i + 1, len(keys1)):
        if keys1[i] > keys1[j]:
            keys1[i],keys1[j] = keys1[j], keys1[i] # Swapping

sorted_key = {} # initialize a blank dictionary
for key in keys1:
    sorted_key[key] = dict1[key]

print("\t|> Sorted Dictionary For Loop Method: ", sorted_key)
