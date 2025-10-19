# to add two complex numbers using Dunder function
#it couse the operator Overloding

# This code demonstrates operator overloading in Python using a class to represent complex numbers.
#Dunder functions are used to define the behavior of operators for user-defined classes.



class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):                 #Dunder function '__add__'
        numReal = self.real + num2.real
        numImg = self.img + num2.img
        return Complex (numReal , numImg)
    
    def __sub__(self,num2):                 #Dunder function '__sub__'
        numReal = self.real - num2.real
        numImg = self.img - num2.img
        return Complex (numReal , numImg)
    
    def __mul__(self,num2):                 #Dunder function '__mul___'
        numReal = self.real * num2.real
        numImg = self.img * num2.img
        return Complex (numReal , numImg)

num1 = Complex(3,7)
num1.showNum()

num2 = Complex(8,9)
num2.showNum()

num3 = num1 + num2
num3.showNum()

num3 = num1 - num2
num3.showNum()

num3 = num1 * num2
num3.showNum()