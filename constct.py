#constructor is a special method which is used to initialize the object of the class.
# It is called when an object of the class is created.
# It is used to set the initial values of the object attributes.
# It is also used to create the object of the class.


class Car:
    #default constructore
    def __init__(self):   # Self is  an object
        print("creating a new car...")
    model = 1989
    series = "s1"

c1 = Car()
print(c1.model,"Model")

c2 = Car()
print(c2.series,"Series")


#create another class

class Student:
                    #paramiterized constructore
    def __init__(self,name,Reg):
        self.name = name    #obj attr > class attr
        self.Reg =Reg
    school = "ABCD School"
    

s1 = Student("Karan",102)
print(s1.name,s1.Reg,"from",s1.school)

s2 = Student("Vinod",103)
print(s2.name,s2.Reg,s2.school)
