#in python we can raise the constome errors by using "raise" keyword

a = int(input("Enter the number between 10 and 15 : "))

if a<10 or a>15:
    raise ValueError("YOU ARE NOT ENTERED number between 10 and 15!") #raise the error
else:
    print("Wow! you enter the number between 10 and 15") #if the number is between 10 and 15 then this will execute