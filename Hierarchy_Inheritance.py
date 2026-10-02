class A:
    def funct1(self):
        print("|> Class 'A' Function Calling -> Hello sir i'm Jarvis.")
    
class B(A):
    def funct2(self):
        print("|> Class 'B' Function Calling -> Hello sir i'm Friday.")
    
class C(A):
    def funct3(self):
        print("|> Class 'C' Function Callin -> Hello sir i'm E.D.I.T.H.")
    
print("-" * 70)
cha = A()
cha.funct1()

print("-" * 70)
chb = B()
chb.funct1()
chb.funct2()

print("-" * 70)
chc = C()
chc.funct1()
chc.funct3()
print("-" * 70)