x =[3,6,3,8]
print(dir(x)) # it will show all the attributes and methods of the list class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p =Person("John", 30)
print(p.__dict__) # it will show the attributes of the list class
print(help(p)) # it will show the documentation of the list class