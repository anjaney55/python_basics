with open("sample.txt","r") as f:
    data = f.read()
    print(data) 

import os

os.remove("sample.txt") 