sum_of = lambda a, b: a + b
sub_of = lambda a, b: a - b
mul_of = lambda a, b: a * b
div_of = lambda a, b: a / b
modula_div_of = lambda a, b: a % b
floar_div_of = lambda a, b: a // b

print("="*40)
num1 = int(input("|> Enter your 1st Num: "))
num2 = int(input("|> Enter your 2nd Num: "))

print("\t|> Sum of your num: ", sum_of(num1, num2))
print("\t|> Sub of your num: ", sub_of(num1, num2))
print("\t|> Mul of your num: ", mul_of(num1, num2))
print("\t|> div of your num: ", div_of(num1, num2))
print("\t|> Modula div of your num: ", modula_div_of(num1, num2))
print("\t|> Floar div of your num: ", floar_div_of(num1, num2))
print("="*40)