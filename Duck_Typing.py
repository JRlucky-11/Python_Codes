class Person:
    def Fun1(slef):
        print("Person") # Duck Typing
        
class Student(Person):
    def Fun1(self):
        print("Student")

def Call_Fun_1(OBJ):
    OBJ.Fun1()

Call_Fun_1(Student())
Call_Fun_1(Person())