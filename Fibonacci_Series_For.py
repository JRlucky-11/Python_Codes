num = int(input("Enter Num: "))
frist_num = 0
second_num = 1
final_num = 0

for i in range(1, num + 1):
    final_num = frist_num + second_num
    frist_num = second_num
    second_num = final_num
    print("\t|> ", final_num, end = " ")
