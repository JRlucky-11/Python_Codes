print("_"*60)
Mobilegrp = { "Mob1" : {"Name1": "Oppo_A5s", "Price1": 12000}, "Mob2" : {"Name2": "Oppo_F27_5G", "Price2" : 21000}}
print("|> 1st Mobile Name: ", Mobilegrp["Mob1"]["Name1"])
print("\t|> Price: ", Mobilegrp["Mob1"]["Price1"])
print("|> 2nd Mobile Name: ", Mobilegrp["Mob2"]["Name2"])
print("\t|> Price: ", Mobilegrp["Mob2"]["Price2"])

print("")
print("_"*60)
str1 = "[ Print all Keys & Values Using For Loop ]"
print(str1.center(60, '-'))
print("_"*60)

for key,value in Mobilegrp.items():
    print(f"key-> {key}, value-> {value}")  # print all key & values in Dictionary.

print("_"*60)
print("")

print("|> Print All Items using Function: ", Mobilegrp.items())    # parin all items.
print("_"*151)

# for main_key, sub_dict in Mobilegrp.items():
#     print(f"Main Key -> {main_key}")
#     for sub_key, sub_value in sub_dict.items():
#         print(f"\t|> {sub_key} : {sub_value}")
        
#     print("-" * 30)
