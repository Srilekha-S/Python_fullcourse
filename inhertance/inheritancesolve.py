class Animal:
    def sound(self):
        print("Animal make sound")
class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")
a1=Animal()
a1.sound()
d1=Dog()
d1.sound()
