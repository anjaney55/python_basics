#how to use import modules these are all the built in fuction we can use 

from math import sqrt,pi
result = sqrt(9) * pi
print(result)

import math as m
res = m.sqrt(16)
print(res)

import math
print(dir(math)) # it will print the all methods and variable in math module 

from yoo import welcome,yoo  #we can use our own module we can use * for all methods 
welcome()
print(yoo)