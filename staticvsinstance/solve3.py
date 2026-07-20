'''Create an Employee class.

Requirements:

name and salary → instance variables
increment_percentage = 10 → class variable
Method to calculate new salary after increment.

Challenge: Change the increment percentage for all employees at once.'''


class Employee:
    increement_percentage = 10
    def __init__(self, name, salary):
        self.name =name
        self.salary = salary
    def salaryincree(self):
        total_salary = self.salary * Employee.increement_percentage / 100
        final_amount = self.salary + total_salary
        print(" A", self.name, "employee's salary is",self.salary, "and he has been paid of with increement",final_amount)
e1 = Employee("Alice", 10000)
e1.salaryincree()