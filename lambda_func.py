# def double(x):
#     return x*3

#functions are passed as a function object to another function
# lambda functions are anonymous functions
# lambda functions are used to create small anonymous functions at runtime

def smll_func(fx, value):
    return 6+fx(value)

double = lambda x: x*5

cube = lambda x: x*x*x

avg = lambda x,y: (x+y)/2

print(cube(5))
print(double(5))

print(avg(4,6))

print(smll_func(double, 5)) # passing function object to another function
print(smll_func(cube, 5))
print(smll_func(avg, 5))