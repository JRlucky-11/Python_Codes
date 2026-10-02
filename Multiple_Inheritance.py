class A:
    def funct1(self):
        print("|> Iron Man -> Tony Stark. I Am Iron-Man.")
    
class B:
    def funct2(self):
        print("|> AI -> JARVIS. Hello Sir... I Am Jarvis.")
    
class C(A,B):
    def funct3(self):
        print("|> AI -> ULTRON. Created by Mistake Jarvis & Tony.")

print("-" * 70)
cha = A()
cha.funct1()

print("-" * 70)
chb = B()
chb.funct2()

print("-" * 70)
chc = C()
# chc.funct1()
# chc.funct2()
chc.funct3()
print("-" * 70)