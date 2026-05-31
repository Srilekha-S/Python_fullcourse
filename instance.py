class Person:
    #using self. is instance variable 
    # i can't give 10 to 15 values to self.name and self.age 
    # because they are instance variables and they are specific to 
    # each object created from the class. Each object can have its own 
    # unique values for these variables. If I want to create multiple 
    # objects with different names and ages, I can do so by creating 
    # multiple instances of the Person class and assigning different 
    # values to the instance variables for each object. For example:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def Sleep(self):
        a=5
        print(self.name, "is sleeping for", a,"hours" )
    
p1=Person("Srilekha", 22)
p1.Sleep()