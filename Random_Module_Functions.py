import random as r1
print(f"|> Ludo dice roll 1 to 6: {r1.randint(1,6)}")

print("")
phones = ["Oppo F27 5g", "Oppo A5s", "Vivo T4x", "Realme P4r", "Samsung Galexy S26 Ultra", "Iqoo Neo 10r"]
print(f"|> Sir Phone List Mein ye saare Elements hai: {phones}")
print(f"\t|>> I Select This Phone: {r1.choice(phones)}")

print("")
print(f"|> Sir Mein 1-100 se ye Number {r1.randint(1,100)} Randomly Choose kiya hai.")

print("")
print(f"|> Sir 1-50 ke Beech 1 Even Number: {r1.randrange(2,51,2)}")