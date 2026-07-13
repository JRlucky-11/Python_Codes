num = int(input("Enter Your Num: "))
chek = 0
i  = 1
while(i <= num):
    if(num % i == 0):
        print("|> Devisible by: ", i)
    i += 1

print("\n")
if(chek == 2):
    print("> It is Prime Num.")
else:
    print("> Not a Prime Num.")
