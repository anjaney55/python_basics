# Super key is used to access the parent class properties and methods in child class.
# It is used to call the parent class constructor in child class.

# It is used to call the parent class methods in child class.
# It is used to call the parent class properties in child class.

class Car :

    def __init__(self,type):
        self.type = type


    @staticmethod
    def start():
        print("car was started...")

    @staticmethod
    def stop():
        print("Car was stoped!")

class TataCar(Car):   #inherite the Car class Single inheritance
    def __init__(self,name,type):
        self.name = name
        
        super().__init__(type)  #Super key is used to parent class properties inherite

        super().start() 


c1 = TataCar("maruti","electric")
print(c1.type)
