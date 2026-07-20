class Student:
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1
s1 = Student("Alice")
s2 = Student("Bob")
print(Student.count)  # Output: 2

#should increase the count variable by 1 for each student created? Yes, the count variable is a class variable that keeps track of the number of Student instances created. Each time a new Student instance is created, the __init__ method is called, which increments the count variable by 1. Therefore, after creating two Student instances (s1 and s2), the count variable will be equal to 2.