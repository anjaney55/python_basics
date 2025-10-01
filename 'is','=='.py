
# The 'is' operator checks if two variables point to the same object in memory
# The '==' operator checks if the values of two variables are equal

# a = (1,2,3)
# b = (1,2,3)
# print(a is b) # True, because they are the same object in memory
# print(a == b) # True, because they have the same value


a =[123, 2, 3]
b =[123, 2, 3]
print(a is b) # False, because they are different objects in memory
print(a == b) # True, because they have the same value
