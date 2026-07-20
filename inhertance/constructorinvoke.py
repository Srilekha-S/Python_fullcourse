class Parent:
    def __init__(self, Networth):
        self.Networth = Networth
class Child(Parent):
    def __init__(self, Networth):
        super().__init__(Networth)
        print(f"Networth of the child is {self.Networth}")
    def ChildNetworth(self):
        print(f"Networth of the child is {self.Networth//2}")
c1 = Child(1000000)

c1.ChildNetworth()  
print(c1.Networth)

#in this code we are using the super() function to call the __init__ method of the parent class and pass the Networth argument to it. This allows us to initialize the Networth attribute in the parent class and then use it in the child class. 
#instead of using self.networth we are using init method