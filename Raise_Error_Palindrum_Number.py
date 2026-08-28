print("~" * 100)
num = int(input("Enter your Number to Check: "))

print("- " * 30)
print(f"|> The Number '{num}' Checking...")
print("- " * 30)

if str(num) == str(num)[::-1]:
    print(f"Confirm '{num}' It is a Palindrum Number.")
else:
    raise ValueError("\t|>> No, it is not Palindrome Number. Please Check!")
print("~" * 100)