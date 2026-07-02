amt = int(input("|> Enter the amount of bike: "))

if amt > 200000:
    print("\t|> The bike is expensive.")
    amt = amt + (15/100 * amt)
    print("\t|> The price of bike after 15% tax is:", amt)
elif amt < 200000 and amt > 100000:
    print("\t|> The bike is moderate.")
    amt = amt + (10/100 * amt)
    print("\t|> The price of bike after 10% tax is:", amt)
else:
    print("\t|> The bike is affordable.")
    amt = amt + (5/100 * amt)
    print("\t|> The price of bike after 5% tax is:", amt)

print("\t|> Enjoy Your Bike. Thank You for visiting our showroom.")