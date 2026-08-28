from functools import reduce
print("="*70)
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("|> Your List is: ", num)

odd = filter(lambda i: i % 2 != 0, num)
# total= reduce(lambda x, y: x + y, num)
print("\t|> Odd Numbers in this list: ", list(odd))

sqr = list(map(lambda x: x * x, num))
print("\t|> Sqr of all Numbers: ", sqr)

total = reduce(lambda x, y: x + y, sqr)
print("\t|> Sum of all sqr Numbers: ", total)
print("="*70)
