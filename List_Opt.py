a = [1,'a', 25.5, True, "Hello World", 3, 6]

print("|> a of [0]: ", a[0])

print("|> a of [1]: ", a[1])

print("|> a: ", a)

a[1] = 'b' # Updated...
print("|> a of [1](Updated value -> b): ", a[1])

print("|> a of [2]: ", a[2])

print("|> a of [3]: ", a[3])

print("|> Updeted a: ", a) # Updated Values...

a.append(12)
print("|> Last Element append -> 12: ", a) # Append 12..

a.insert(5, 'xyz')
print("|> Insert -> 'xyz': ", a) # Insert 'xyz'

a.remove(3)
print("|> Remove -> 3: ", a) # Remove

a.pop()
print("|> Pop: ", a) # POP

print("|> Lenth of List: ", len(a)) # Lenth

a.pop(3)
print("|> Pop3 -> 3: ", a) # Pop 3

del a[2]
print("|> Del:", a)

# del a
# print("|> Deleted:", a)
print("\n")

a2 = [1,3,2,1,3,4,6]
print("|> a2:", a2)

a2.clear()
print("|> Clear:", a2)
print("\n")

a3 = [10, 21, 310, 'xyz', 'abc', 292]
a3.reverse()
print("|> Rev: ", a3)
print("|> Rev ind: ", a3[::-1])
print("\n")

a4 = ['a', 'ball', 'A']
a4.sort(reverse = False)
print("|> Decending to Assending Order: ", a4)
a4.sort(reverse = True)
print("|> Assending to Dessending Order: ", a4)
print("\n")