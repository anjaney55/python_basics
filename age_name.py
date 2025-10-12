name=input("Enter a name: ")
age=input("Enter an age: ")

print(f"Hello {name}, you are {age} years old.") if age.isdigit() else print("Invalid input")