str1 = "! Hello Programmer, Welcome to Queue Operation [FIFO] !"
str2 = "1. Enqueue (Add Element)"
str3 = "2. Dequeue (Remove Element)"
str4 = "3. Peek (View Top Element)"
str5 = "4. Display (All Elements)"
str6 = "5. Exit"
str7 = "! Menu !"

print("="* 120)
print(str1.center(120, '='))

size = int(input("|> Eneter Size of Queue: ")) # input size of list
Queue = []
ch = 0
value = 0

while(ch != 5):
    print(str7.center(120, '-'))
    print(">", str2)
    print(">", str3)
    print(">", str4)
    print(">", str5)
    print(">", str6)
    print("")

    ch = int(input("|> Enter Option: "))
    print("")

    if(ch == 1):
        print("\t|>> You Selected Enqueue Operation.")
        if (len(Queue) == size):
            print("\t\t|>>> Queue Overflow..!")
        else:
            value = int(input("\t\t|>>> Enter Value to Enqueue: "))
            Queue.append(value)
            print("\t\t|>>> Added Seccessfully.")
    elif(ch == 2):
        print("\t|>> You Selected Dequeue Operation.")
        if(len(Queue) == 0):
            print("\t\t|>>> Queue Underflow..!")
        else:
            remove = Queue.pop(0)
            print("\t\t|>>> Removed Element: ", remove)
            print("\t\t|>>> Removed Successfully")
    elif(ch == 3):
        print("\t|>> You Selected Peek Operation.")
        if(len(Queue) == 0):
            print("\t\t|>>> Queue is Empty..!")
        else:
            print("\t\t|>>> front Element: ", Queue[0])
    elif(ch == 4):
        print("\t|>> You Selected Display Operation.")
        if(len(Queue) == 0):
            print("\t\t|>>> Queue is Empty..!")
        else:
            print("\t\t|>>> Queue Elements: ", Queue)
    elif(ch == 5):
        print("\t|>> Exiting....")
    else:
        print("\t|>> Invalid Optiion...! Try Again.")

print("="* 120)