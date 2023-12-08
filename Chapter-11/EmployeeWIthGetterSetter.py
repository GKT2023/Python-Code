class Employee:
    salary = 100
    increment = 10
    def __init__(self,salary,increment):
        self.salary = 100
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,increment):
        return self.salary + increment
    

e = Employee(100,10)
print(e.salary)
print(e.increment)
e.increment = 80
print(e.increment)
print(e.salaryAfterIncrement)