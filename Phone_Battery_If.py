bat = int(input("\n|> What is the Battery Percentage?=> "))
if bat >= 80:
    print("\t|>> Your Battery is in Good Condition.")
elif bat >= 50:
    print("\t|>> Your Battery is in Average Condition.")
else:
    print("\t|>> Your Battery is Dead. Please Connect Your Charger.\n")