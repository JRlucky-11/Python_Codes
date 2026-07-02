a = "Python"
print(a)
del a
# a = "123" # if you uncomment this line, it will create a new variable 'a' with the value "123"
print(a)  # This will raise a NameError since 'a' has been deleted
