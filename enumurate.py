#Enumerete Fuction 
# Enumerate is a built-in function in Python that adds a counter to an iterable and returns it as an enumerate object.
# This is useful when you need a counter with the values in the iterable, such as when iterating over a list or tuple.
# The enumerate object can be converted to a list or tuple, or you can iterate over it directly in a for loop.


marks = [56,67,89,100,76,87,53,64]

for index, mark in enumerate(marks,start=1): #we can start the idx by specific by default is 0 
    print(mark)
    if(index==3):
        print("Awsome!")


