
'''Define Employee class with attributes role,department & salary.This class also show the showDetails() method
        Create an Engineer class the inherits the Employee & it includes attributes : name & age'''

class Employee:
    def __init__(self,role,dept,sal):
        self.role = role
        self.dept = dept
        self.sal = sal

    def showDetails(self):
        print("role = ",self.role)
        print("department = ",self.dept)
        print("salary = ",self.sal)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Accountant","Finance","45,000") #calling parent class constructor 

e1 = Employee("Engineer","Development","70,000")
e1.showDetails()

e2 = Engineer("Arun","35")
print("name = ",e2.name)
print("age = ",e2.age)
e2.showDetails()