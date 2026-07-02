sz1 = int(input("|> Enter the first side of triangle: "))
sz2 = int(input("|> Enter the second side of triangle: "))
sz3 = int(input("|> Enter the third side of triangle: "))


if sz1 == sz2 == sz3:
    print("\t|> The triangle is an Equilateral triangle.")
elif sz1 == sz2 or sz2 == sz3 or sz1 == sz3:
    print("\t|> The triangle is an Isosceles triangle.")
else:
    print("\t|> The triangle is a Scalene triangle.")


