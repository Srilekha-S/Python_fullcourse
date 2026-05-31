class Person:
    sleeping_hours = 8
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    @classmethod
    def Sleep(cls):
        print("person should sleep for atleast", cls.sleeping_hours, "hours a day")

    #def eat(self):
        #print(Person.sleeping_hours) Actually it won't work because eat is not a class method and it is trying to access the class variable sleeping_hours without using the class name or cls.
Person.Sleep()
#Person.eat()


#We can't access static variables in instance method without using the class name or cls. We can access static variables in class method using cls. We can access static variables in static method using the class name.
##static = class level variable
#instance = object level variable