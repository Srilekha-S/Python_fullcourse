class Person:
    
    sleepingtime = 5#static variable
    def __init__(self, name, age):
        self.name = name
        self.age =  age
        self.sleepingtime= 8 # instance varible
p1 =Person("Alice", 30)
print(p1.sleepingtime)#object use instance variable
print(Person.sleepingtime)#class use static variable