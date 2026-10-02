# class A:
#     def Show(self):
#         print("A")
# class B(A):
#     def Show(self):
#         print("B")
# class C(A):
#     def Show(self): # Dimond Problem
#         print("C")
# class D(C,B):
#     # def Show(self):
#     #     print("D")
#     pass
    
# obj1 = D()
# obj1.Show()
# print(D.mro()) # Method Resolution Order

# class Person:
#     def __init__ (self, name):
#         self.name = name
# class Student(Person):
#     def __init__(self, Ainame, name):
#             super().__init__(name)
#             self.Ainame = Ainame

# s1 = Student("Tony", "Jarvis") 
# print(s1.Ainame)
# print(s1.name)

# Employee Name
# MRO