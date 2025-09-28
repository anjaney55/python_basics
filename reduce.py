
from functools import reduce

# This program uses the reduce function to sum all the elements in a list
# The reduce function takes a function and a sequence as arguments
# It applies the function cumulatively to the items of the sequence, from left to right, so as to reduce the sequence to a single value


# Example: sum of all elements in a list
list = [1,2,3,4,5]

def sum(x,y):
    return x+y

result= reduce (sum,list)

print(result) # Output: 15