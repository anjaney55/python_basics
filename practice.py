
'''create a clss of student which takes name & marks of 3 subject as argument in constructore then create a method to print average of marks'''

class Student:

    def __init__(self,name,m1,m2,m3):
        self.name = name
        self.m1 = m1 
        self.m2 = m2 
        self.m3 = m3

    def avg (self,m1,m2,m3):
        sum = m1+m2+m3
        avg = sum/3
        return avg 

s1 = Student("kiran",76,87,54)
print(s1.name)
print("average marks is ",s1.avg(76,86,54)) 
        

#Another method
class Man:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_Avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("Hi",self.name,"Your avarage marks is ",sum/3)
    
m1 = Man("Vinod",[98,52,99])
m1.get_Avg()