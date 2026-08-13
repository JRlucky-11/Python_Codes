print("="*100)

Name = ["apple", "ball", "cat", "elephant", "aeroplane", "bat", "dog", "egg"]
print("|> Your all Names: ", Name)
print("-"*100)
frist_letters = [names[0].lower() for names in Name]
print("\t|> All Frist Letters are: ", frist_letters)

unique_letters = list(set(frist_letters))
unique_letters.sort()
print("\t|> Unique Letters are: ", unique_letters)

print("\t|> Letter Counts:")
for letter in unique_letters:
    count = frist_letters.count(letter)
    print(f"\t\t|>> {letter} found {count} times..!")
    
print("="*100)