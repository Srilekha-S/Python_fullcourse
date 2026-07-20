class Person:
    sleeping_hours = 8

    def __init__(self, name, age):
        self.name =  name
        self.age= age
        
    @staticmethod
    def Sleep():
        print("A person should be sleep for atleast", Person.sleeping_hours, "hours a day")

    def eat(self):
        print("A person should eat healthy food and sleep for atleast", Person.sleeping_hours, "hours a day")
print(Person.sleeping_hours)
person1 = Person("alice", 30)
person1.Sleep()
person1.eat()
 