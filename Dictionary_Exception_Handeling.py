str1 = "! Hello Programmer, Welcome to Dictionary Operation !" 
str2 = "1. Clear"
str3 = "2. Copy"
str4 = "3. Fromkeys"
str5 = "4. Get"
str6 = "5. Items"
str7 = "6. Keys"
str8 = "7. Pop"
str9 = "8. Popitem"
str10 = "9. Setdefault"
str11 = "10. Update"
str12 = "11. Values"
str14 = "e/E for Exit"
str13 = "! Menu !"

print("\n")
print("=" * 100)
print(str1.center(100, '='))
dict1 = {"Device": "Oppo F27 5g", "Battery": "5000mah", "Charging Type": "Type-C"}
print(str13.center(100, '-'))
print("|> Your Dictionary is -> ", dict1)
print("", str2, "\n", str3, "\n", str4, "\n", str5, "\n", str6, "\n", str7, "\n", str8, "\n", str9, "\n", str10, "\n", str11, "\n", str12, "\n", str14, "\n")

while True:
    try:
        ch = input("|> Choose Your Option (1-11): ")
        print("=" * 100)

        if ch == 1:
            print("\t|>> Selected Clear Option.")

            dict1.clear()
            print("\t\t|>>> Dictionary Cleared ->", dict1)

        elif ch == 2:
            print("\t|>> Selected Copy Option.")

            new_dict = dict1.copy()
            print("\t\t|>>> Copied Dictionary ->", new_dict)

        elif ch == 3:
            print("\t|>> Selected Fromkeys Option.")

            keys_input = input("\t\t|>>> Enter keys separated by space: ").split()
            default_val = input("\t\t|>>> Enter common value for all keys: ")
            res = dict.fromkeys(keys_input, default_val)
            print("\t\t\t|>>>> New Dictionary fromkeys ->", res)

        elif ch == 4:
            print("\t|>> Selected Get Function.")

            key = input("\t\t|>>> Enter key to get value: ")
            print("\t\t|>>>> Value ->", dict1.get(key, "Key Not Found!"))

        elif ch == 5:
            print("\t|>> Selected Items Option.")

            print("\t\t|>>> Items ->", list(dict1.items()))

        elif ch == 6:
            print("\t|>> Selected Clear Option.")

            print("\t\t|>>> Keys ->", list(dict1.keys()))

        elif ch == 7:
            print("\t|>> Selected Pop Option.")

            print("\t\t|>>> Available Keys:", list(dict1.keys()))
            key = input("\t\t\t|>>>> Which Key you Should be remove in this Dictionary?: ")
            if key in dict1:
                removed_val = dict1.pop(key)
                print(f"\t\t\t\t|>>>>> Removed '{key}': '{removed_val}'")
                print("\t\t\t\t|>>>>> Updated Dictionary ->", dict1)
            else:
                print("\t\t\t\t|>>>>> This Key is not Present in this Dictionary!")

        elif ch == 8:
            print("\t|>> Selected Popitem Option.")

            confirm = input("\t\t|>>> Remove Last item? (yes/no): ").lower()
            if confirm == "yes":
                if dict1:
                    item = dict1.popitem()
                    print("\t\t\t|>>>> Removed Item ->", item)
                    print("\t\t\t|>>>> Updated Dictionary ->", dict1)
                else:
                    print("\t\t\t|>>>> Dictionary is Empty!")
            else:
                print("\t\t|>>> Operation Cancelled.")

        elif ch == 9:
            print("\t|>> Selected Setdefault Option.")

            key = input("\t\t|>>> Key check/add?: ")
            val = input("\t\t|>>> Value set?: ")
            result = dict1.setdefault(key, val)
            print("\t\t|>>> Result Value ->", result)
            print("\t\t|>>> Updated Dictionary ->", dict1)

        elif ch == 10:
            print("\t|>> Selected Update Option.")

            mode = input("\t\t|>>> Update? (1. Existing Key Change / 2. New Key Add): ")
            if mode == "1":
                print("\t\t\t|>>>> Current Keys:", list(dict1.keys()))
                key = input("\t\t\t|>>>> Which keys Value change?: ")
                if key in dict1:
                    new_val = input(f"\t\t\t\t|>>>>> Enter new value for '{key}': ")
                    dict1.update({key: new_val})
                    print("\t\t\t\t|>>>>> Updated Dictionary ->", dict1)
                else:
                    print("\t\t\t\t|>>>>> Key not found!")
            elif mode == "2":
                new_key = input("\t\t\t|>>>> New Key name: ")
                new_val = input("\t\t\t|>>>> New Key value: ")
                dict1.update({new_key: new_val})
                print("\t\t\t|>>>> Updated Dictionary ->", dict1)
            else:
                print("\t\t\t|>>>> Invalid Choice!")

        elif ch == 11:
            print("\t|>> Selected Values Option.")

            print("\t\t|>>> Values ->", list(dict1.values()))
        
        elif ch == "e" and "E":
            print("\t|>> Exiting the Program...")
            break

        else:
            print("\t|>> Invalid Option Selected!")

    except Exception as e:
        print(f"Error Find -> {e}")
print("=" * 100)