unit = int(input("|> Enter the electricity unit: "))
meterbill = 30
bill = 0
print("\t|> Electricity unit: $", unit)

if unit > 150:
    units = unit - 150
    bill = (50 * 2.50) + (100 * 5.00) + (units * 7.00)
elif unit > 50 and unit <= 150:
    units = unit - 50
    bill = (50 * 2.50) + (units * 5.00)
elif unit <= 50:
    bill = unit * 2.50
else:
    print("\t|> Invalid input")
    
totalbill = bill + meterbill
print("\t|> Total electricity bill: $", totalbill)