class School:
    def __init__(self):
        self.Name = "ABC School"
        self.Place = "XYZ City"
        self.__Revenue = 1000000
    def __PrivateMethod(self):
        return self.__Revenue
    def PublicMethod(self):
        return self.__PrivateMethod()
s1 = School()
print(s1.Name)
print(s1.Place)
print(s1.PublicMethod())  # This line will return the private method value since it is been accessed in the public method.
