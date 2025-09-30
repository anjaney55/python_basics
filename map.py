#map function in python
# The map() function in Python is used to apply a function to all the items in an input list (or any iterable).
# It returns a map object (which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.).
# You can convert the map object to a list or tuple using the list() or tuple() functions.

# Syntax:
# map(function, iterable, ...)
def sqr(x):
    return x*x

l =[1,2,3,4,5]

new_list = list(map(sqr,l))# using map function to apply sqr to each element in l

print(new_list)