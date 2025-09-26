

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
#     print("END")

# show(5)

# #to print factorial

# a = int(input("enter the number : "))

# def facto(n):
#     if(n==0 or n==1):
#         return 1
    
#     return n*facto(n-1)
    

# print("factorial = ",facto(5))


#to print sum


def calc_sum(a):
    if(a==0):
        return 0
    
    return calc_sum(a-1)+a

print(calc_sum(5))