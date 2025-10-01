#Instance variables are variables that are bound to the instance of the class. They are defined inside the __init__ method and are prefixed with self. Instance variables are unique to each instance of the class, meaning that each object can have different values for these variables.
# Class variables are variables that are shared among all instances of the class. They are defined outside of any method and are prefixed with the class name. Class variables are not unique to each instance, meaning that if one instance changes the value of a class variable, it will affect all other instances of the class.
# In this example, we will create a class called Employee with an instance variable called name and a class variable called raise_amount. We will then create two instances of the Employee class and show how the instance variable and class variable work.

class Employee:
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.1

    def show_details(self):
        print(f"Employee name is {self.name} and raised amount is {self.raise_amount}")

e1=Employee("John")
e1.raise_amount=0.2 # changing the raise amount for e1 instance
e1.show_details()
e2=Employee("Doe")
Employee.show_details(e2)