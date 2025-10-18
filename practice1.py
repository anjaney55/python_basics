
'''Define a circle class to create a circle with the radius r using constructor
    Define Area() method to claculate the area of the circle
    Define a Perimeter method to claculate the perimeter of the circle'''

class Circle:
    def __init__(self,red):
        self.red = red

    def Area(self):
        return 3.14 * self.red *self.red
    
    def Perimeter(self):
        return 2 * 3.14 * self.red
    
c1 = Circle(6)
print("Area of the circle is ",c1.Area())
print("Perimeter is ",c1.Perimeter())