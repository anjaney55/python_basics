# Private variables in Python are not truly private, but they are name-mangled to prevent accidental access.
# This means that you can still access them if you know the mangled name, but it is not recommended to do so.
# Private variables are typically prefixed with two underscores (__) to indicate that they are intended for internal use only.
#
# In this example, we define a class Account with a private variable __acc_pass.    

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass   # '__' private key  

    def reset_pass(self): # this method is used to reset the password
        print(self.__acc_pass) # it is used to access the private variable

a1 = Account("1234","74cd")
print(a1.acc_no)

print(a1.reset_pass()) # it is used to access the private variable
# print(a1.__acc_pass) # it is used to access the private variable, but it will give an error because it is private
# print(a1._Account__acc_pass) # it is used to access the private variable, but it is not recommended to do so
#

    