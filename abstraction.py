
#Absrtaction is hiding the unneccessary data from the user 

class Car:
    def __init__ (self):
        self.acc = False
        self.brk = False
        self.cluch = False

    def start(self):
        self.cluch = True   
        self.acc = True
        print("Car started....")

c1 = Car()
c1.start()