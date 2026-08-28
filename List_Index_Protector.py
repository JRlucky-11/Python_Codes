mobile_brand = ["Oppo", "Vivo", "Motorola", "Samsung", "Mi-Poco", "Apple", "Techno", "Infinix"]
print("="*110)
print("|> Your List is: ", mobile_brand)
print("-"*110)

while True:
    idx = input("\t|>> Enter Index no to Check ('exit' to Exit the Program...): ")
    
    if idx == 'Exit':
        print("\t\t|>>> Exiting the List_Index Potector Program...")
        break

    try:
        print("\t|>> Index Value: ", mobile_brand[int(idx)])
        print("~"*110)
        break
    except IndexError as idxe:
        print(f"\t|>> Error: This Index {idxe} is not Availabel ! Try Again...")
        print("~"*110)
    except ValueError as ve:
        # 3. String/text inputs ko catch karne ke liye
        print(f"\t|>> Error: Invalid input [{ve}]. Enter a Valid Number or 'Exit'...! Try Again...")
        print("~"*110)

print("="*110)