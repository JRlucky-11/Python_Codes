class Person:
    def __init__ (self, name):
        self.name = name
class Student(Person):
    def __init__(self, Ainame, name):
            super().__init__(name) # Constucter inherit 
            self.Ainame = Ainame

s1 = Student("Karen", "Spiderman") 
print(f"Ai Name: {s1.Ainame}")
print(f"Using Character: {s1.name}")
