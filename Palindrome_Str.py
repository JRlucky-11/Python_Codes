str1 = input("|> Enter String: ")
str2 = str1[::-1]
if(str1 == str2):
    print("\t|>> It is a Palindrom.")
else:
    print("\t|>> No, It is a normal String.")