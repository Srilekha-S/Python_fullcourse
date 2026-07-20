class School:
    def __init__(self):
        self.Name = "ABC School"
        self.Place = "XYZ City"
        self.__Revenue = 1000000
    def SchoolRevenue(self):
        return self.__Revenue
s1 = School()
print(s1.Name)
print(s1.Place)
print(s1.SchoolRevenue())
#print(s1.__Revenue) this can't be run since it is private variable.
print(s1._School__Revenue)  # This line will return the private variable value.      