import random

def check(user, comp):
    if user == comp:
        return 0
    
    elif(user==0 and comp==2):
        return 1
    
    elif(user==2 and comp==0):
        return -1
    
    elif(user==1 and comp==2):
        return -1
    
    elif(user==2 and comp==1):
        return 1
    
    elif(user==0 and comp==1):
        return -1
    
    elif(user==1 and comp==0):
        return 1
    
    return 1

user = (input("Enter your choice (0. water, 2. gun, 1.snake)")) 
comp = random.randint(0, 2)

score = check(user, comp)

if score == 0:
    print("It's a tie!")

elif score == 1:
    print("You win!")   

elif score == -1:   
    print("You lose!")
else:
    print("Invalid input!")
# The code implements a simple game where the user can choose between three options: water, gun, and snake.

print("User choice:", user)
print("Computer choice:", comp)
print("Score:", score)


