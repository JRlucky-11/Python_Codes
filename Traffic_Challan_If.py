print("\n===================================")
print("\t___***Challan Status***___")
name = input("|> Enter Your Name: ")
ph_no = int(input("|> Enter Your Phone Number: "))
speed = int(input("|> Enter Vheicle Speed: "))
total = 0
reason = ""

if(speed >= 80):
    total = total + 1000
    reason = reason + "\t\t> Over Speed...!\n"

ch = input("|> Helmet Using -> Yes or No |=> ")
if(ch == 'No' or ch == 'no'):
    total = total + 1000
    reason = reason + "\t\t> Riding Without Helmet.\n"

ch1 = input("|> Submit Valid Vheicle Papers? -> Yes or No |=> ")
if(ch1 == 'No' or ch1 == 'no'):
    total = total + 5000
    reason = reason + "\t\t> Invalid / No Vheicle Papers.\n"

ch2 = input("|> Driving Licence Using? -> Yes or No |=> ")
if(ch2 == 'No' or ch2 == 'no'):
    total = total + 5000
    reason = reason + "\t\t> Driving Without Licence.\n"

ch3 = input("|> PUC Certificate Verified? -> Yes or No |=> ")
if(ch3 == 'No' or ch3 == 'no'):
    total = total + 5000
    reason = reason + "\t\t> Without PUC Certificate.\n"

ch4 = input("|> RC Using? -> Yes or No |=> ")
if(ch4 == 'No' or ch4 == 'no'):
    total = total + 5000
    reason = reason + "\t\t> RC not Available.\n"

print("-----------------------------------")
print("\t___Bill Status___")
print("|> Name:", name)
print("|> Mobile Number:", ph_no)
if total == 0:
    print(name, "\t|>> Hello here is no Challan. Safe Driver!")
else:
    print("\t|>>", name, "Your Challan is Pending...")
    print("\t|>> Your Speed => ", speed, "km/h")
    print("\t|>> Your Mistakes:\n", reason)
    print("\t|>> Total bill = $", total)
print("===================================")