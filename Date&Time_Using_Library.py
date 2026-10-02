from datetime import date

y = int(input("Enter Birth Year: "))
m = int(input("Enter Birth Month: "))
d = int(input("Enter Birth Day: "))

today = date.today()
birth_date = date(y, m, d)

years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

print(years, months, days)