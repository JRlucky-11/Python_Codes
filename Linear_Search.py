str1 = "! Hello Programmer, Welcome to Linear Search !"
str2 = "[WARNING: If Your Target is Matched Then Return Target's Index Value..Neither Return a Negetive Value..!]"

print("="* 120)
print(str1.center(120, '='))
print(str2.center(120))

size = int(input("|> Eneter Size of List: ")) # input size of list
print("")
list2 = [int(input("\t> Enter " + str(i+1) + " Element: ")) for i in range(0,size)]
print("")
print("|> Your List: ", list2)

print("")
target = int(input("|> Enter Your Target to Search in this List: "))
print("\t> Target Locked -> ", target, "<--")
print("")

found = False

for i in range(0, size):
    if(list2[i] == target):
        print("\t\t>> Target Found at Index: ", i)
        found = True

if not found:
    print("\t> No Value Found in This List...!")
    print("\t> Mission Unsuccessful")

print("="* 120)