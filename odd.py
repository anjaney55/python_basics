n = int(input("enter the number : "))

def num(a):
    if(a%2==0):
        return "EVEN"
    elif(a%2!=0):
        return "ODD"
    else:
        return "ERROR"

result =num(n)
print(result)
