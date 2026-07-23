str1 = "[ Welcome To The Number Guessing Game! ]"
str2 = "! Hello User, Please Guess a Number 1 to 100 !"
str3 = "...! CONGRATULATIONS! You guessed it right GAME OVER !..."

print("="* 100)
print(str1.center(100))
print("="* 100)
print(str2.center(100, "-"))

mynum = 40
usernum = 0
i = 0

while(usernum != mynum):
    usernum = int(input("|> Enter Your Number: "))
    i += 1

    if (usernum > mynum):
        print("\t>> Too High! Try a Smaller Number.")
    elif(usernum < mynum):
        print("\t>> Too Low! Try a Larger Number.")
    else:
        print("-"* 100)
        print(str3.center(100))
        print("\t> My Number is: ", mynum)
        print("\t> Your Attemps: ", i)
print("-"* 100)
