class Bird:
    def fly(self):
        print("Bird can fly")
class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")
p1=Penguin()
p1.fly()

