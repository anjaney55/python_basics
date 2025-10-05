def welcome():
    print("hay welcome to my program!")

'''Idiom is a comman pattern used in python scripts to determine whether the scripts is being run directly or imported as a module into another script'''

print(__name__)

if __name__ == "__main__":  # the code is ruunning through this function the welcome() function will call otherwise it will not call when another program was use this module
    welcome()