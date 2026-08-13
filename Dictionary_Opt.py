laptopdict = {"Name": "Yoga_Slim_7i_OLED", "Ram": 8, "Rom": 1024, }
print("|> Your Dictionary: ", laptopdict)
print("|> Name: ", laptopdict["Name"], "\n")

laptopdict["Name"] = "Asus_Vivobook_S16_OLED"   # Update Key -> "Name" Value.
print("|> Update_Name: ", laptopdict["Name"])
laptopdict.update({"Ram": 16, "Price": 85000})  # Update Key -> "Ram" & add Key -> "Price".
print("|> Update_Ram_&_Add_Price: ", laptopdict["Ram"])
print("\t\t|>> Price: ", laptopdict["Price"], "\n")

laptopdict["Mob_No"] = 7608806244               # Add new Key -> "Mob_No".
print("|> Add_(Mob_No): ", laptopdict["Mob_No"], "\n")

print("|> Keys are: ", laptopdict.keys(), "\n")          # print all Keys.

print("|> Values are: ", laptopdict.values(), "\n")      # print all Values.

print("|> Get_Key_Name: ", laptopdict.get("Name"), "\n") # print Key -> "Name" Value.

print("|> Pop_Key_Name: ", laptopdict.pop("Rom"))  # Popped Key -> "Rom" Value.
print("|> Popped only Rom: ", laptopdict, "\n")

print("|> Pop_Item: ", laptopdict.popitem())       # Popped last Key & Value
print("|> Popped Last Item: ", laptopdict, "\n")

laptop2 = laptopdict.copy()
print("|> Copied to another Variable(1st Method): ", laptop2)   # Copy 1st Method
laptop1 = laptopdict
print("|> Copied to another Variable(2nd Method): ", laptop1)   # Copy 2nd Method

