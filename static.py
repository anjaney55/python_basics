#decorator is a special type of function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.
# # It is used to add functionality to an existing function in a clean and readable way.
# # It is used to modify the behavior of a function or class.

class My:
    def __init__(self):
        print("Hi everyone!")

    @staticmethod     #decorator for static method
    def welcome():   # it not used self parameter 
        print("Welcome to all")

m1 = My()
print(m1.welcome()) # it is not used self parameter
# it is used class name to call the static method
# it is not used instance name to call the static method
