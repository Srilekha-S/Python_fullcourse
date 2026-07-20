#singe level and heirarchical inheritance and multiple inheritance combined.

class GrandParent():
    def swim(self):
        print("swimming")
class Relative(GrandParent):
    def sport(self):
        print("playing")
class Parent(GrandParent):
    def sing(self):
        print("parent is singing")
class Child(Parent,GrandParent):
    def dance(self):
        print("child is dancing")