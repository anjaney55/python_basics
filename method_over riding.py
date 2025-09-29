# Method Overriding in Python
# Method overriding is a feature that allows a subclass to provide a specific implementation of a method that is already defined in its superclass.
# When a method in a subclass has the same name and signature as a method in its superclass, the subclass's method overrides the superclass's method.
# This allows the subclass to provide its own behavior while still maintaining the interface of the superclass.
# In Python, method overriding is achieved by defining a method in the subclass with the same name as the method in the superclass.
# The subclass's method will be called instead of the superclass's method when an instance of the subclass is created and the method is called.


class Shape:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def area(self):
        return self.x * self.y
    
class Circle(Shape):  # Inheriting from Shape
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)

    def area(self): # Overriding the area method
        return 3.14 * super().area()

c = Circle(5)
print(c.area())  # Output: 78.5

# rect = Shape(10, 20)
# print(rect.area())  
