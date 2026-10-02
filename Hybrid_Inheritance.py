class a:
    def fun1(self):
        print("|> Jarvis")
class b(a):
    def fun2(self):
        print("|> Tony Stark Access Jarvis. (All time Owner)")
class c(a):
    def fun3(self):
        print("|> Bruece banner Access Jarvis. (2012)")
class d(b,c):
    def fun4(self):
        print("|> Vision Access Jarvis. (Age of Ultron)")

print("-" * 50)
a1 = a()
a1.fun1()

print("-" * 50)
b1 = b()
# b1.fun1()
b1.fun2()

print("-" * 50)
c1 = c()
# c1.fun1()
c1.fun3()

print("-" * 50)
d1 = d()
# d1.fun1()
# d1.fun2()
# d1.fun3()
d1.fun4()
print("-" * 50)