# # Filter (Function, iterable)
number = [1,2,3,4,5,6]

even = filter(lambda i: i % 2 == 0, number)
# print(even) # not print the value
print("Your List is: ", number) # print the Object.
print("Your Even Numbers in list: ", list(even))