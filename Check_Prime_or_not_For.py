num = int(input("Enter Your Num: "))
chek = 0
for i in range(1, num+1):
    if(num % i == 0):
        chek = chek + 1
        print("|> Devisible by: ", i)

print("\n")
if(chek == 2):
    print("> It is Prime Num.")
else:
    print("> Not a Prime Num.")
