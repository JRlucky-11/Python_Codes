number = [1,2,3,4,5,6,7]

even_sqr = {numbers: numbers * numbers for numbers in number if numbers % 2 == 0}
print(even_sqr)