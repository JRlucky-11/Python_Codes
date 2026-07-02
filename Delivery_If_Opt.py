oder =int(input("|> Oder Price: "))
if (oder > 1000):
    print("\t|>> No delivery Charges can be applied.")
    print("\t|>> Total Amount: ", oder)
elif(oder >= 500 and oder <= 1000):
    print("\t|>> Delivery Charges: 50")
    print("\t|>> Total Amount: ", oder + 50)
else:
    print("\t|>> Delivery Charges: 100")
    print("\t|>> Total Amount: ", oder + 100)