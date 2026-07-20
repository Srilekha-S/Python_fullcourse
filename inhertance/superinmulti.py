class Parent:
    def  Sing(self):
        print("Parent's skill is singing")
class Relative:
    def Sing(self):
        print("Relative's skill is singing")
    def Dance(self):
        print("Relative's skill is dancing")
'''
class Child(Parent, Relative):
    def common(self):
        print("Child's skill is singing and dancing")
'''
#super keyword
class Child(Parent, Relative):
    def common(self):
        super(Parent, self).Sing()# this super keyword skip the class
        pass  # This will show the method resolution order for the Child class
c1 = Child()
c1.Sing()  # This will call the Sing method from the Parent class due to the order of inheritance
#Relative.Sing(c1) using class name means it need to be static and this line works since we pass object as an argument to the method and it will call the Sing method from the Relative class
Child.common(c1)  # This will call the common method which uses super to call the Sing method from the Parent class

#print(Child.__mro__)

