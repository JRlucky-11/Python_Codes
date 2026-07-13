num = int(input("Enter a Num: "))
check = 0
reminder = 0
sum = 0

check = num
i = 1
while(i <= num):
    reminder = num % 10
    sum = (sum * 10) + reminder
    num = num // 10
    i += 1

if (sum == check):
    print("Yes, It is a Palindrome Number.")
else:
    print("No, it is not Palindrome Number.")