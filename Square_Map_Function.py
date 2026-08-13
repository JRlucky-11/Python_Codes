# Map ... Map ( Function, iterable[list,tupple])
number = [1,2,3,4,5,6]
sqr = map(lambda num: num * num, number)
# print(sqr) # Not print the value
print("Your Square Number is: ", number) # print the Object.
print("Your Square is: ", list(sqr)) # print the Value.