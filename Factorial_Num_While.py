num = int(input("Enter a num: "))
i = 1
fact = 1

while (i <= num):
    fact = fact * i
    i = i+1
    print(fact)
    i += 1
    
print("Factorial of", num, ":", fact)