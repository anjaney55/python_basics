x = 10

def hi():
    global x,y
    x = 20
    y = 30
    print("Hello")

hi()
print(x)
# print(y)  # This will raise an error because y is not defined in the global scope
# The variable y is defined inside the function hi() and is not accessible outside of it.