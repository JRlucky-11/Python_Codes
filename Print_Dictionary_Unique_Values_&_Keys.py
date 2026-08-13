print("_"*75)
dict1 = {'a':5, 'b':2, 'c':5, 'd':10}
print("|> Your 1st Dictionary is: ", dict1)

laptopdict = {"Name": "Yoga_Slim_7i_OLED", "Ram": 8, "Rom": 1024, }
print("|> Your 2nd Dictionary is: ", laptopdict)

print("\t|> Print only Unique Values: ", set[dict1.values()]) # print Unique Values
print("\t|> Print Unique Keys: ", dict1.keys())              # print Unique Keys

dict1.update(laptopdict)
print("Your Merge Dictionary is: ", dict1)
print("_"*75)