str1 = "! Hello Programmer, Welcome to Binary Search !"
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

st_idx = 0
en_idx = size - 1
mid_idx = 0
found = False

while(st_idx <= en_idx):
    mid_idx = (st_idx + en_idx) // 2
    if(list2[mid_idx] == target):
        print("\t\t>> Target Found at Index: ", mid_idx)
        print("\t\t>> Mission Successful")
        found = True
        break
    elif(list2[mid_idx] > target):
        en_idx = mid_idx - 1
    else:
        st_idx = mid_idx + 1

if not found:
    print("\t> No Value Found in This List...!")
    print("\t> Mission Unsuccessful")

print("="* 120)