std1 = {"Name" : "Jasobant Rout", "Home" : "Bisuniapada", "Age" : 21, "Mobile_Brand" : "Oppo"}
print("="*110)
print("|> Your Dictionary is: ", std1)
print("-"*110)

while True:
    key = input("\t|>> Enter key Name ('exit' to Exit the Program...): ")

    if key == 'exit':
        print("\t\t|>>> Exiting the Dictionary LookUp Program...")
        break

    try:
        print("\t|>> Value: ", std1[key])
        print("~"*110)
        break
    except KeyError as Error:
        print(f"\t|>> Error: Key {Error} is not Availabel ! Try Again...")
        print("~"*110)
    
print("="*110)