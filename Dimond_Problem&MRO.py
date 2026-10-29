class A:
    def Show(self):
        print("A")
class B(A):
    def Show(self):
        print("B")
class C(A):
    def Show(self): # Dimond Problem
        print("C")
class D(C,B):
    # def Show(self):
    #     print("D")
    pass
    
obj1 = D()
obj1.Show()
print(D.mro()) # Method Resolution Order