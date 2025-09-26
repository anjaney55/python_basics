# This code demonstrates the use of class methods in Python.
# Class methods are methods that are bound to the class and not the instance of the class. They can be called on the class itself, rather than on instances of the class. Class methods are defined using the @classmethod decorator and take a reference to the class as their first argument (usually named cls). 
# This allows them to access class-level attributes and methods.
# Class methods are often used for factory methods, which are methods that return an instance of the class. They can also be used to modify class-level attributes or perform operations that are related to the class as a whole, rather than to individual instances.
#
# In this example, we define a class called Employee with a class method called changeCompany. The changeCompany method takes a new company name as an argument and changes the company name for all instances of the Employee class. We create an instance of the Employee class, call the show method to display the employee's name and company, change the company name using the changeCompany method, and then call the show method again to display the updated information.

class Employee:
    company ="Apple"
    def show(self):
        print(f"Employee name is {self.name} and company is {self.company}")

    @classmethod # This is a class method that can be called on the class itself, not just on instances of the class.
    def changeCompany(self,changeCompany):
        self.company = changeCompany # This method changes the company name for all instances of the class.

e1 = Employee()
e1.name = "Ajay"
e1.show()
e1.changeCompany("Tesla")
e1.show()
print(Employee.company)