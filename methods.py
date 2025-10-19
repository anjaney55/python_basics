class Human:
    def __init__(self,fname):
        print("mention new type of Human....")
        self.fname = fname


    def doctore(self,name):
        print(self.fname ,name,"check the patient properly\n")
    
    def engineer(self,name):
        print(self.fname ,name,"to create something new techologies")

    
d1 = Human("Docter")
d1.doctore("Kiran") 

e1 = Human("Engineer")
e1.engineer("Vinod")
