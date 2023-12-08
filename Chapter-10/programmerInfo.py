class Programmer:
    company = 'Microsoft'
    def __init__(self,name,empcode,salary):
        self.name = name
        self.empcode = empcode
        self.salary = salary


p = Programmer("Tom",12345,500000)
print(p.name, p.salary, p.empcode)
print(p.company)
