a = input("|> Enter your sentence: ")
print("========================================================")

print("|> Press '1' -> For check Cases.\n|> Press '2' -> For replace a character in your sentence.\n|> Press '3' -> For check the count of a character in your sentence.\n|> Press '4' -> For check the start and end of your sentence.\n")
ch = int(input("|> Select num 1-4:"))
if(ch == 1):
    print("\t|>> Your sentence is: ", a)
    print("\t|>> Your title case sentence is:", a.title()) # Each word Capital
    print("\t|>> Your capitalized sentence is:", a.capitalize()) # Capital Starting Word
    print("\t|>> Your uppercase sentence is:", a.upper()) # All words are Capital
    print("\t|>> Your lowercase sentence is:", a.lower()) # All words are Lower
elif(ch == 2):
    print("\t|>> Your sentence is: ", a)
    ch1 = input("\t|>> Enter the character you want to replace: ")
    ch2 = input("\t|>> Enter the character you want to replace with: ")
    print("\t|>> Your sentence with '", ch1, "' replaced by '", ch2, "' is:", a.replace(ch1, ch2)) # replace(old, new)
    print("\t\t|>> Your original sentence is:", a)
elif(ch == 3):
    print("\t|>> Your sentence is: ", a)
    ch1 = input("\t|>> Enter the character you want to check the count of: ")
    print("\t|>> The count of '", ch1, "' in your sentence is:", a.count(ch1))
elif(ch == 4):
    print("\t|>> Your sentence is: ", a)
    ch1 = input("\t|>> Enter the character you want to check if your sentence starts with: ")
    ch2 = input("\t|>> Enter the character you want to check if your sentence ends with: ")
    print("\t|>> Does your sentence start with '", ch1, "'? ", a.startswith(ch1))
    print("\t|>> Does your sentence end with '", ch2, "'? ", a.endswith(ch2))
else:
    print("\t|>> Invalid choice. Please select a number between 1 and 4. Run again.")
print("========================================================")