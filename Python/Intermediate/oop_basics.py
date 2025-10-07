# Object-Oriented Programming in Python

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def display(self):
        print(f"Name: {self.name}, Grade: {self.grade}")

# Create objects
s1 = Student("Aarav", "A")
s2 = Student("Diya", "B+")

s1.display()
s2.display()
