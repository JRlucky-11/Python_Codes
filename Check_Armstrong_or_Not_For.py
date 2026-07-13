n = input("Enter num: ")
num = int(n)
arm = 0
reminder = 0
lenth = len(n)
copy = num

for i in range(1, len(str(num)) + 1):
    reminder = num % 10
    arm = arm + reminder**lenth
    num = num // 10

if (copy == arm):
    print("Armstorng!")
else:
   print("Not")