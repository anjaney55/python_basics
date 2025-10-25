#one method to change the class name is we use Person instead of self in function or method
# # Another method is using decorator


class Person :
    name = "Rahul"

    def changeName(self,name): 
        self.__class__.name = "Gagan"  #we cannot change the classs name directly through functions or methods

p1 = Person()
p1.changeName("Gagan")
print(p1.name)
print(Person.name)


#ANother method is using decorator

class Man :
    sub = "Java"

    @classmethod           #Decorator 
    def changeSub(cls,sub): #cls is reference of the class 
        cls.sub = sub

m1 = Man() 
m1.changeSub("Python") #it is used to change the class variable using class method
print(m1.sub) #it is used to change the class variable using instance name
#it is used to change the class variable using class name
print(Man.sub) #it is used to change the class variable using class name