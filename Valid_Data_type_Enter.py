list1 = []
while True:
    b = input("Enter Number: ")
    if b == "Exit":
        break
    else:
        try:
            list1.append(int(b))
        except ValueError as error:
            print("Your Error is: ", "Enter Valid data Type.")
print("List is: ", list1)