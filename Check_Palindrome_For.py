num = int(input("Enter a Num: "))
check = 0
reminder = 0
sum = 0

check = num
# for i in range(1, num + 1)
#     reminder = num % 10
#     sum = (sum * 10) + reminder
#     num = num // 10

# if (sum == check):
#     print("It is a Palindrome Number.")
# else:
#     print("No it is not Palindrome Number.")

for i in range(1, len(str(num)) + 1):
    reminder = num % 10
    sum = (sum * 10) + reminder
    num = num // 10

if (sum == check):
    print("Yes, It is a Palindrome Number.")
else:
    print("No, it is not Palindrome Number.")