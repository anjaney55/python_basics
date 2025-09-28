# This code demonstrates the use of `seek()` and `tell()` methods in file handling in Python.
# The `seek()` method is used to change the file's current position, while the `tell()` method returns the current position in the file.

with open('practice.txt', 'r') as f:
    print(type(f)) #<class '_io.TextIOWrapper'>

    f.seek(10) #move to the 10th bite of the file

    print(f.tell()) # 10th bite of the file

    data = f.read(5) #read 5 bytes from the file
    print(data) # 10th to 15th bite of the file
