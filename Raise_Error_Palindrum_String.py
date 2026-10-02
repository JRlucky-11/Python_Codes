print("~" * 100)
word = input("|> Enter Palindrum String Check Here: ") # ababa
chk_word = word[::-1]

print("- " * 30)
print(f"|> The Word '{word}' Checking...")
print("- " * 30)

if(word == chk_word):
    print(f"\t|>> Confrim '{word}' It is a Plindrum.")
else:
    raise ValueError(f"|>> No, Your String is not Palindrum String. Please Check!")
print("~" * 100)