n = input("Enter num: ")
num = int(n)
arm = 0
reminder = 0
lenth = len(n)
copy = num

while(num > 0):
    reminder = num % 10
    arm = arm + reminder**lenth
    num = num // 10
    i += 1

if (copy == arm):
    print("Armstorng!")
else:
   print("Not")