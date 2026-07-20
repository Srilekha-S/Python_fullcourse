class School:
    def __init__(self):
        self.Name = "ABC School"
        self.Place = "XYZ City"
        self._Revenue = 1000000
class Faculty(School):
    def Revenue(self):
        return self._Revenue
faculty1 = Faculty()
print(faculty1.Name)
print(faculty1.Place)
print(faculty1.Revenue())  # This line will return the protected variable value.

print(faculty1._Revenue)  # This line will also return the protected variable value.