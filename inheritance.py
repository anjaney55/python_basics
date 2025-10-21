
#inheritance is a way to form new classes using classes that have already been defined.
# It helps to reuse the code and make it more readable.
# It is a way to create a new class from an existing class.
# It is a way to create a new class from an existing class by inheriting the properties and methods of the existing class.
# It is a way to create a new class from an existing class by inheriting the properties and methods of the existing class and adding new properties and methods to the new class.
# It is a way to create a new class from an existing class by inheriting the properties and methods of the existing class and adding new properties and methods to the new class and overriding the existing properties and methods of the existing class.



class Car :
    @staticmethod #decorator for static method 
    def start():
        print("car was started...")

    @staticmethod 
    def stop():
        print("Car was stoped!")

class ToyotaCar(Car):   #inherite the Car class Single inheritance 
    def __init__(self,brand):
        self.brand = brand

class Fortunar(ToyotaCar):   #Multi-Level inheritance inherit the TootaCar as well as Car class
    def __init__(self,type):
        self.type = type        

c1 = ToyotaCar("fortunar")
print(c1.brand)

c1 = Fortunar("Petrol")
print(c1.type,"type car")
print(c1.start())


#Multiple inheritance is a feature of object-oriented programming in which a class can inherit attributes and methods from more than one parent class.
# It allows a class to inherit properties and methods from multiple classes, enabling code reuse and flexibility in design.
# It is a way to create a new class from multiple existing classes by inheriting the properties and methods of the existing classes.
# It is a way to create a new class from multiple existing classes by inheriting the properties and methods of the existing classes and adding new properties and methods to the new class.

# It is a way to create a new class from multiple existing classes by inheriting the properties and methods of the existing classes and adding new properties and methods to the new class and overriding the existing properties and methods of the existing classes.
# It is a way to create a new class from multiple existing classes by inheriting the properties and methods of the existing classes and adding new properties and methods to the new class and overriding the existing properties and methods of the existing classes and resolving any conflicts that may arise from multiple inheritance.


class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B): # separated by commas
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)