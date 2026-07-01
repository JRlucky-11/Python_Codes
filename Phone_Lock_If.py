name = input("\n|> Please enter your First Name: ")
phone = input("|> Please enter your Phone Name: ")
lock = int(input("|> Please enter the Lock: "))
if lock == 1234:
    print("\t|>> Lock is Correct! Access granted. Phone Unlocked.")
    print("\t|>> Welcome to your Phone! ", phone)
    print("\t|>> Hello", name, "Aap kya Open karna chahte ho? --[Whatsapp, Instagram, Facebook, Youtube, Google]--")
    open = input("\t\t|>>> Please enter the App Name: ")
    if open == "Whatsapp":
        print("\t\t\t|>>>> Opening Whatsapp...\n")
    elif open == "Instagram":
        print("\t\t\t|>>>> Opening Instagram...\n")
    elif open == "Facebook":
        print("\t\t\t|>>>> Opening Facebook...\n")
    elif open == "Youtube":
        print("\t\t\t|>>>> Opening Youtube...\n")
    elif open == "Google":
        print("\t\t\t|>>>> Opening Google...\n")        
    else:
        print("\t\t|>>> Sorry! This App is actually available in your Phone. But i can't open it because this is a demo version of this program.\n")
else:
    print("\t|>> Lock is Incorrect! Access denied. Phone Locked.")
    print("\t|>> Are you really the owner of this phone? Please Don't Try to Hack it.\n")