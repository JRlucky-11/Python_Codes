num = int(input("Enter Num: "))
arm = 0
store = num
remind = 0
for i in range(1, num):
    remind = num % 10
    arm = (remind * remind * remind) + arm
    num = num // 10

if (store == arm):
    print("It is an Armstrong Number.")
else:
    print("Not an Armstrong Number.")