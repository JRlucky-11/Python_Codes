int1 = 10
int2 = 20
sum_int = int1 + int2
print("|> ", int1, " + ", int2, " = ", sum_int, "Int to Float[Type Casting] -> ", float(sum_int), "\n") # Int to Float type casting

float1 = 1.4
float2 = 2.5
sum = float1 + float2
print("|> ", float1, " + ", float2, " = ", sum, "Float to Int[Type Casting] -> ", int(sum), "\n") # Float to Int type casting

str1 = '14342'
print("|> ", "My String is: " , str1 , " String Type", type(str1))
var1 = int(str1) # String to Int type casting
print("\t|>> ", "String to Int[Type Casting]: ", var1, "Int Type", type(var1), "\n")

str2 = '12.34'
print("|> ", "My String is: " , str2 , " String Type", type(str2))
var2 = float(str2) # String to Float type casting
print("\t|>> ", "String to Float[Type Casting]: ", var2, "Float Type", type(var2), "\n")

in1 = 1234
print("|> ", "My Int is: " , in1 , " Int Type", type(in1))
var3 = str(in1) # Int to String type casting
print("\t|>> ", "Int to String[Type Casting]: ", var3, "String Type", type(var3), "\n")

fl1 = 13.56
print("|> ", "My Float is: " , fl1 , " Float Type", type(fl1))
var4 = str(fl1) # Float to String type casting
print("\t|>> ", "Float to String[Type Casting]: ", var4, "String Type", type(var4), "\n")