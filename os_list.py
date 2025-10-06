#this program lists all the folders in the Tutorials directory and prints the contents of each folder


import os

folders = os.listdir("Tutorials")
print(folders)

print(os.getcwd())

for folder in folders:
    print(folder)
    print(os.listdir(f"Tutorials/{folder}"))

