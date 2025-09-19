
#Ternary Operator

food = (input("Enter the food name :"))

eat = "Yes cake is available" if food=="cake" else "No there is no cake "
print(eat)


age = int(input("Enter your age : "))

print("your eligible") if age>=18 and age<100 else print("your are not eligible")

#Clever if / ternary operator

vote = ("Yes" , "No") [age<18]
print(vote)

# to add tax to salary
salary = float(input("Enter your salary :"))

tax = salary*(0.1 , 0.2) [salary>=50000]

print(tax)