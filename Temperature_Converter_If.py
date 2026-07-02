num = int(input("|> Enter the Number: "))
print("\t|> What Action you want to perform: ")
print("\t|> 1. Celsius to Fahrenheit")
print("\t|> 2. Fahrenheit to Celsius")

choice = int(input("\t|> Enter your choice: "))
if choice == 1:
    fahr = (num * 9/5) + 32
    print("\t|>> Temperature in Fahrenheit:", fahr)
elif choice == 2:
    cels = (num - 32) * 5/9
    print("\t|>> Temperature in Celsius:", cels)
else:
    print("\t|>> Invalid choice. Please select 1 or 2. Run Again..!")
