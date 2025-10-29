#This code deletes a folder and its contents if it exists. If the folder does not exist, it prints a message indicating that the folder was not found.

import os

if(os.path.exists("Tutorials")):
    print("Folder found")
    os.remove("Tutorials/a.png")
    print("Folder deleted")

else:
    print("Folder not found")










