print("="*35)
num = int(input("Enter any integer number: "))

binary_val = bin(num)
octal_val = oct(num)
hex_val = hex(num)

print("="*35)
print(f"Decimal Value     : {num}")
print(f"Binary Value      : {binary_val[2:]}")
print(f"Octal Value       : {octal_val[2:]}")
print(f"Hexadecimal Value : {hex_val[2:].upper()}")
print("="*35)