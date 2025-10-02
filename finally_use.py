#*j*Finally Clause means it always exucuted errorr ho naa hoo
def func():
    try:
        l = [1,2,4,5,7]
        i = int(input("Eneter the index: "))
        print(l[i])
        return 1

    except :
        print("some error occured")
        return 0

    finally:  #when we are not using finally clause the remain code will not executed when it is in the function
        #when we use the finally it always executed
        print("I am always executed")

x = func()
print(x)