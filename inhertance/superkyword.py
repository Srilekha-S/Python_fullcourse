class parent:
    def drive(self,speed):
        print(f"driving at {speed} mph")
class child(parent):
    def drive(self,speed):
        super().drive(speed)
        print(f"child is driving at {speed - 20} mph")
c1=child()
c1.drive(50)