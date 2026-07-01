year = int(input("Enter the Year: "))
if(year % 4 == 0):
    if(year / 100 != 0):
        print("Yes, It is a Leap Year...")
else:
    print("No, It is not a Leap Year.")