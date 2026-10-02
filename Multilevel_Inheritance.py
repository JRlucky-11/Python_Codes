class A:
    def funct1(self):
        print("|> Tony Stark in Iron Man 2008. Hero")
    
class B(A):
    def funct2(self):
        print("|> Tony Stark in Hulk 2008. Post Credit Scene.")
    
class C(B):
    def funct3(self):
        print("|> Tony Stark in The Avengers 2012. Hero.")

print("-" * 70)
a1 = A()
a1.funct1()

print("-" * 70)
b1 = B()
# b1.funct1()
b1.funct2()

print("-" * 70)
c1 = C()
# c1.funct1()
# c1.funct2()
c1.funct3()
print("-" * 70)