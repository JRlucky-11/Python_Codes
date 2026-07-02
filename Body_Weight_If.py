print("\n=====================================")
print("__Hello, Welcome to Weight Checker__")
print("=====================================")
name =finput("|> What is Your name: ")
print("\t|>> Hello,", name, "\n\t\tHave a Nice Day...!")
print("--------------------------------------")
weight = float(input("PLease Say What is Your Weight: "))
print("|>> Your Health Report:")
print("______________________________________")
if weight < 50.00:
    print("Underweight..! \n[Aapka weight bohot kaam hai, \nplease acha khana khaiye...]")
elif weight >= 50.00 and weight <= 80.00:
    print("Healthy Weight..! \n[WOW! Healthy life, \nChill Bro....]")
elif weight > 80.00 and weight <= 120.00:
    print("Overweight..! \n[Aapka weight thoda zyada hai, \nPlease Start the Exercise...]")
else:
    print("Please Enter Valid Weight format..!!! & Run again this Code...")
print("--------------------------------------")
print("Thank you, Visit Again...!")
print("======================================\n")