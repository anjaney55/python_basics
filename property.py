# Property Decorator in Python
# Property decorator is used to create a method as a property of class.

class Student :
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.prc = (self.phy+self.chem+self.math)/3


s1 = Student(98,97,95)
print(s1.prc)

s1.chem = 79
print(s1.prc) #the percentage will not change 

#property 

class Std :
    def __init__(self,kan,eng,hindi):
        self.kan = kan
        self.eng = eng
        self.hindi = hindi

    @property  #we can use methods as a property by using property decorator
    #it is used to create a property in class
    #it is used to create a method as a property
    #it is used to create a method as a property of class

    def percentage(self):
        return str((self.kan+self.eng+self.hindi)/3) + "%"

p1 = Std(98,97,95)
print(p1.percentage)

p1.eng = 79
print(p1.percentage)