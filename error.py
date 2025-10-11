import sys
user = input("Enter a number : ")

try:
    number = int(user)
except ValueError:
    print("You are not entered a number sorry!...")
    sys.exit(1)

print(f"You entered number is {user}")

    