a = [1,'a', 25.5, True, "Hello World", 3, 6]
print("|> Your List: ", a)

del a[2]
print("|> Del:", a) # Delete index[2] value.in

del a
print("|> Deleted:", a) # list was deleted (NameError)