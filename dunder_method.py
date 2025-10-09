#Magic/Dunder methods
# Magic methods are special methods in Python that start and end with double underscores (dunder).
# They are also known as "dunder" methods. These methods allow you to define the behavior of your objects for built-in operations such as addition, subtraction, and string representation.
# Magic methods are not called directly, but are invoked by Python when you perform certain operations on objects.
# For example, when you use the `+` operator on two objects, Python will call the `__add__` method of the first object and pass the second object as an argument.
# Magic methods allow you to customize the behavior of your objects and make them behave like built-in types.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Magic method for string representation
    def __str__(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}" # This method is called when you use print() on an object of this class

    # Magic method for addition
    def __add__(self, other):
        return self.salary + other.salary # Assuming you want to add salaries

    # Magic method for equality
    def __eq__(self, other):
        return self.salary == other.salary 
    
e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)
print(e1)  # Calls __str__ method
print(e2)  # Calls __str__ method
print(e1 + e2)  # Calls __add__ method
print(e1 == e2)  # Calls __eq__ method
print(e1.__dict__)  # Accessing the __dict__ attribute directly
print(e1.__class__)  # Accessing the __class__ attribute