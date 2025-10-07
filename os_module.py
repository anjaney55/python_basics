#os module is used to interact with the operating system
#it is used to create folders, delete folders, rename folders, etc
#it is used to perform operations on files and folders
#it is used to get the current working directory, change the current working directory, etc
#we can delete the files and folders using this module for example if we want to delete the folder we can use os.rmdir() method
#we can delete the file using os.remove() method
#we can rename the file using os.rename() method
#we can rename the folder using os.rename() method
#we can get the current working directory using os.getcwd() method
#we can change the current working directory using os.chdir() method
#we can create the folder using os.mkdir() method
#to enter the folder we can use os.chdir() method
#we can get the list of files and folders in the current working directory using os.listdir() method



#this program creates a folder named Tutorials and creates 20 folders in it named Day1, Day2, Day3, ..., Day20
import os

if(not os.path.exists("Tutorials")):  #it will check whether folder is exists it will not execute if not it will execute
    os.mkdir("Tutorials")

for i in range(1,21):
    os.mkdir(f"Tutorials/Day{i}")   #it will create the 20 new folders in Tutorials at a time 
    