
l=[3,7,4,2,1,3,6,8,9]

def filter_func(a):
    return a>4

# filter function in python
# The filter() function in Python is used to construct an iterator from elements of an iterable for which a function returns true.
# It filters the given iterable with the help of a function that tests each element in the iterable to be true or not.
# It returns an iterator from those elements of the iterable for which the function returns true.
# Syntax:
# filter(function, iterable)

newlist=list(filter(filter_func,l))# using filter function to apply filter_func to each element in l

print(newlist)