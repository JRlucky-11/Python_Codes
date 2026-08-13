import random

str1 = "[ Welcome To NUMBER GUESSING GAME! ]"
str2 = "! Hello User, Please Guess a Number 1 to 100 !"
str3 = "...! CONGRATULATIONS! You guessed it right GAME OVER !..."

print("="* 100)
print(str1.center(100))
print("="* 100)
print(str2.center(100, "-"))

mynum = random.randint(1,100)
usernum = 0
i = 0

while(usernum != mynum):
    usernum = int(input("|> Enter Your Number: "))
    i += 1

    if (usernum > mynum):
        print("\t>> Too High!\n\tTry a Smaller Number.")
    elif(usernum < mynum):
        print("\t>> Too Low!\n\tTry a Larger Number.")
    else:
        print("-"* 100)
        print(str3.center(100))
        print("\t> My Number is: ", mynum)
        print("\t> Your Attemps: ", i)
        break
print("-"* 100)
