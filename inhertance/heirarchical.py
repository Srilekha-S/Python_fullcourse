class GrandParent():
    def swim(self):
        print("swimming")
class Parent(GrandParent ):
    def __init__(self,networth):
        self.networth = 1000000
    def sing(self):
        print("parent is singing")
class Child(GrandParent):
    def dance(self):
        print("child is dancing")
c1 = Child(1000000)
c1.sing()  # Output: parent is singing
c1.dance()  # Output: child is dancing
c1.swim()  # Output: swimming