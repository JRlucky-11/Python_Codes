class student:
    my = "Hello"
    def __init__(self, name, age): # Constructer, instance Variable
        print("Hello Sir")
        self.name = name
        self.age = age

N = input("Enter Your Name: ") # Input Name & Age
A = int(input("Enter Your Age: "))

s1 = student(N, A)

print(f"{student.my} User..!")
print(f"I am {s1.name}")
print(f"My age {s1.age}") 